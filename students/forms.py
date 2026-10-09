from django import forms
from .models import StudentProfile
from accounts.forms import UserUpdateForm

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=["college","degree","branch","graduation_year","phone","skills","bio","resume","linkedin","github"]
        widgets={"bio":forms.Textarea(attrs={"rows":4}),"skills":forms.TextInput(attrs={"placeholder":"Python, Django, SQL, Java"})}
        def __init__(self,*args,**kwargs): super().__init__(*args,**kwargs)
