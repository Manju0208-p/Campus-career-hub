from django.contrib import admin
from .models import RecruiterProfile
@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display=("company_name","user","industry","location","verified")
    list_filter=("verified","industry")
    search_fields=("company_name","user__username")
