from django.contrib import admin
from .models import (
    Profile,
    Expertise,
    Project,
    PosterDesign,
    BrandBoardDeliverable,
    WorkStep,
    ContactMessage
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
