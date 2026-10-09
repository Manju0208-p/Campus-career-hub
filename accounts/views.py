from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from students.models import StudentProfile
from recruiters.models import RecruiterProfile

class CareerLoginView(LoginView):
    template_name="accounts/login.html"
    authentication_form=UserLoginForm

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            if user.user_type=="student": StudentProfile.objects.create(user=user)
            else: RecruiterProfile.objects.create(user=user)
            login(request,user)
            messages.success(request,"Account created successfully. Complete your profile to get started.")
            return redirect("dashboard:home")
    else: form=UserRegisterForm()
    return render(request,"accounts/register.html",{"form":form})

@login_required
def profile(request):
    if request.user.user_type=="student": return redirect("students:profile")
    return redirect("recruiters:profile")

@login_required
def edit_account(request):
    if request.method=="POST":
        form=UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid(): form.save(); messages.success(request,"Account details updated."); return redirect("accounts:profile")
    else: form=UserUpdateForm(instance=request.user)
    return render(request,"accounts/edit_account.html",{"form":form})
