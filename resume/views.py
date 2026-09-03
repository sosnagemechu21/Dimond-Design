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
    ContactMessage,
    BrandingQuestionnaire
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


@require_POST
def questionnaire_submit(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST

        full_name = data.get('full_name', '').strip()
        email = data.get('email', '').strip()
        phone_or_whatsapp = data.get('phone_or_whatsapp', '').strip()
        brand_name = data.get('brand_name', '').strip()
        industry = data.get('industry', '').strip()
        brand_stage = data.get('brand_stage', '').strip()
        services_selected = data.get('services_selected', '')
        if isinstance(services_selected, list):
            services_selected = ', '.join(services_selected)
        else:
            services_selected = str(services_selected).strip()

        brand_vibe = data.get('brand_vibe', '')
        if isinstance(brand_vibe, list):
            brand_vibe = ', '.join(brand_vibe)
        else:
            brand_vibe = str(brand_vibe).strip()

        color_preferences = data.get('color_preferences', '').strip()
        target_audience = data.get('target_audience', '').strip()
        timeline = data.get('timeline', '').strip()
        project_description = data.get('project_description', '').strip()

        if not full_name or not email or not brand_name:
            return JsonResponse({
                'status': 'error',
                'message': 'Please provide your name, email, and brand name.'
            }, status=400)

        brief = BrandingQuestionnaire.objects.create(
            full_name=full_name,
            email=email,
            phone_or_whatsapp=phone_or_whatsapp,
            brand_name=brand_name,
            industry=industry,
            brand_stage=brand_stage,
            services_selected=services_selected,
            brand_vibe=brand_vibe,
            color_preferences=color_preferences,
            target_audience=target_audience,
            timeline=timeline,
            project_description=project_description,
        )

        profile = Profile.objects.first()
        whatsapp_raw = profile.whatsapp_number.replace('+', '').replace(' ', '') if profile else "251984670908"
        wa_text = f"Hi Dagim! I just submitted my Branding Discovery Brief for *{brand_name}* on your website. My name is {full_name}."
        from urllib.parse import quote
        wa_link = f"https://wa.me/{whatsapp_raw}?text={quote(wa_text)}"

        return JsonResponse({
            'status': 'success',
            'brief_id': brief.id,
            'brand_name': brief.brand_name,
            'whatsapp_link': wa_link,
            'message': f"Thank you, {full_name}! Your discovery brief for {brand_name} has been received. Dagim will review it and get back to you within 24 hours."
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Could not submit brief: {str(e)}'
        }, status=500)
