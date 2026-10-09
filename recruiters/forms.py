from django import forms
from .models import RecruiterProfile

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model=RecruiterProfile
        fields=["company_name","company_website","company_description","industry","location","phone"]
        widgets={"company_description":forms.Textarea(attrs={"rows":4})}
