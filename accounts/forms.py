from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","user_type","password1","password2"]

class UserLoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]
        widgets={f:forms.TextInput(attrs={"class":"form-control"}) for f in ["first_name","last_name","email"]}
