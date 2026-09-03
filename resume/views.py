import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import (
    Profile,
    Expertise,
    Project,
    PosterDesign,
    BrandBoardDeliverable,
    WorkStep,
    ContactMessage
)

def index(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(name="Dagim", brand_name="Diamond Design")

    expertise_list = Expertise.objects.all()
    projects = Project.objects.filter(is_featured=True)
    posters = PosterDesign.objects.all()
    deliverables = BrandBoardDeliverable.objects.all()
    work_steps = WorkStep.objects.all()

    context = {
        'profile': profile,
        'expertise_list': expertise_list,
        'projects': projects,
        'posters': posters,
        'deliverables': deliverables,
        'work_steps': work_steps,
    }
    return render(request, 'resume/index.html', context)


@require_POST
def contact_submit(request):
    try:
        # Check if JSON payload or form data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            service = data.get('service', '').strip()
            message = data.get('message', '').strip()
        else:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            service = request.POST.get('service', '').strip()
            message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            return JsonResponse({
                'status': 'error',
                'message': 'Please provide your name, email, and message.'
            }, status=400)

        ContactMessage.objects.create(
            name=name,
            email=email,
            service_needed=service,
            message=message
        )

        return JsonResponse({
            'status': 'success',
            'message': 'Thank you! Your message has been sent to Dagim. We will be in touch within 24 hours.'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Could not send message: {str(e)}'
        }, status=500)
