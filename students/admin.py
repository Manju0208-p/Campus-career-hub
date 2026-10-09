from django.contrib import admin
from .models import StudentProfile
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display=("user","college","branch","graduation_year")
    search_fields=("user__username","user__email","skills","college")
