from django.contrib import admin
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

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand_name', 'title', 'whatsapp_display', 'brands_shipped_count')

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')
    list_editable = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'category', 'year', 'order', 'is_featured')
    list_editable = ('order', 'is_featured')
    search_fields = ('title', 'category', 'client')

@admin.register(PosterDesign)
class PosterDesignAdmin(admin.ModelAdmin):
    list_display = ('brand', 'category', 'year', 'order')
    list_editable = ('order',)
    search_fields = ('brand', 'category')

@admin.register(BrandBoardDeliverable)
class BrandBoardDeliverableAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(WorkStep)
class WorkStepAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')
    list_editable = ('order',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_needed', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')

@admin.register(BrandingQuestionnaire)
class BrandingQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'full_name', 'email', 'phone_or_whatsapp', 'industry', 'timeline', 'status', 'created_at')
    list_filter = ('status', 'timeline', 'brand_stage', 'created_at')
    search_fields = ('brand_name', 'full_name', 'email', 'phone_or_whatsapp', 'industry', 'project_description')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ("Founder & Brand Info", {
            'fields': ('full_name', 'email', 'phone_or_whatsapp', 'brand_name', 'industry', 'brand_stage')
        }),
        ("Design Preferences & Direction", {
            'fields': ('services_selected', 'brand_vibe', 'color_preferences', 'target_audience')
        }),
        ("Timeline & Project Scope", {
            'fields': ('timeline', 'project_description', 'status', 'created_at')
        }),
    )

