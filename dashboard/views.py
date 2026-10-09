from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from jobs.models import Job, Application
from students.models import StudentProfile
from recruiters.models import RecruiterProfile

def home(request):
    jobs=Job.objects.filter(is_active=True).select_related("recruiter")[:6]
    return render(request,"dashboard/home.html",{"jobs":jobs})

@login_required
def dashboard(request):
    if request.user.user_type=="student":
        profile,_=StudentProfile.objects.get_or_create(user=request.user)
        apps=Application.objects.filter(student=request.user)
        recommended=Job.objects.filter(is_active=True).select_related("recruiter")[:6]
        return render(request,"dashboard/student.html",{"profile":profile,"applications":apps,"recommended":recommended})
    profile,_=RecruiterProfile.objects.get_or_create(user=request.user,defaults={"company_name":request.user.username+" Company"})
    jobs=Job.objects.filter(recruiter=profile)
    apps=Application.objects.filter(job__recruiter=profile)
    return render(request,"dashboard/recruiter.html",{"profile":profile,"jobs":jobs,"applications":apps})
