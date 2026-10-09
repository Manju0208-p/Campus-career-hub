from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from jobs.models import Job, Application
from .models import RecruiterProfile
from .forms import RecruiterProfileForm

def recruiter_required(view):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated or request.user.user_type!="recruiter": return redirect("dashboard:home")
        return view(request,*args,**kwargs)
    return wrapper

@login_required
@recruiter_required
def profile(request):
    profile,_=RecruiterProfile.objects.get_or_create(user=request.user,defaults={"company_name":request.user.username+" Company"})
    if request.method=="POST":
        form=RecruiterProfileForm(request.POST,instance=profile)
        if form.is_valid(): form.save(); messages.success(request,"Company profile updated."); return redirect("recruiters:profile")
    else: form=RecruiterProfileForm(instance=profile)
    return render(request,"recruiters/profile.html",{"form":form,"profile":profile})

@login_required
@recruiter_required
def dashboard(request):
    profile=get_object_or_404(RecruiterProfile,user=request.user)
    jobs=Job.objects.filter(recruiter=profile)
    apps=Application.objects.filter(job__recruiter=profile).select_related("student","job")
    return render(request,"recruiters/dashboard.html",{"jobs":jobs,"applications":apps,"profile":profile})

@login_required
@recruiter_required
def applicants(request,job_id):
    job=get_object_or_404(Job,id=job_id,recruiter__user=request.user)
    apps=Application.objects.filter(job=job).select_related("student","student__student_profile")
    return render(request,"recruiters/applicants.html",{"job":job,"applications":apps})

@login_required
@recruiter_required
def update_application(request,application_id):
    app=get_object_or_404(Application,id=application_id,job__recruiter__user=request.user)
    if request.method=="POST":
        status=request.POST.get("status")
        if status in dict(Application.STATUS_CHOICES): app.status=status; app.save(); messages.success(request,"Application status updated.")
    return redirect("recruiters:applicants",job_id=app.job_id)
