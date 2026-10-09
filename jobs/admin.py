from django.contrib import admin
from .models import Job, Application
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=("title","recruiter","job_type","location","deadline","is_active","created_at")
    list_filter=("job_type","is_active")
    search_fields=("title","skills_required","recruiter__company_name")
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display=("job","student","status","applied_at","updated_at")
    list_filter=("status",)
    search_fields=("job__title","student__username","student__email")
