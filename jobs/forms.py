from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=["title","description","skills_required","job_type","location","stipend_or_salary","openings","deadline","is_active"]
        widgets={"description":forms.Textarea(attrs={"rows":5}),"skills_required":forms.TextInput(attrs={"placeholder":"Python, Django, SQL"}),"deadline":forms.DateInput(attrs={"type":"date"})}

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Application
        fields=["cover_note"]
        widgets={"cover_note":forms.Textarea(attrs={"rows":5,"placeholder":"Briefly explain why you are a good fit..."})}
