from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from jobs.models import Job, Application
from .models import StudentProfile
from .forms import StudentProfileForm
from django.db.models import Q
from django.utils import timezone

def student_required(view):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated or request.user.user_type!="student": return redirect("dashboard:home")
        return view(request,*args,**kwargs)
    return wrapper

@login_required
@student_required
def profile(request):
    profile,_=StudentProfile.objects.get_or_create(user=request.user)
    if request.method=="POST":
        form=StudentProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid(): form.save(); messages.success(request,"Student profile updated."); return redirect("students:profile")
    else: form=StudentProfileForm(instance=profile)
    return render(request,"students/profile.html",{"form":form,"profile":profile})

@login_required
@student_required
def applications(request):
    apps=Application.objects.filter(student=request.user).select_related("job","job__recruiter__user")
    return render(request,"students/applications.html",{"applications":apps})

@login_required
@student_required
def recommendations(request):
    profile,_=StudentProfile.objects.get_or_create(user=request.user)

    jobs=Job.objects.filter(
        is_active=True
    ).filter(
        Q(deadline__isnull=True) | Q(deadline__gte=timezone.localdate())
    ).select_related("recruiter__user")

    ranked=[]
    skills=set(profile.skill_list())

    for job in jobs:
        required=set(job.skill_list())
        score=round((len(skills & required)/len(required))*100) if required else 0
        ranked.append((score,job))

    ranked.sort(key=lambda x:(-x[0],-x[1].created_at.timestamp()))

    return render(
        request,
        "students/recommendations.html",
        {"ranked":ranked[:20]}
    )
