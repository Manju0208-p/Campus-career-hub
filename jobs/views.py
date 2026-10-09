from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from recruiters.models import RecruiterProfile
from students.models import StudentProfile
from .models import Job, Application
from .forms import JobForm, ApplicationForm

def jobs_list(request):
    qs=Job.objects.filter(
        is_active=True
    ).filter(
        Q(deadline__isnull=True) | Q(deadline__gte=timezone.localdate())
    ).select_related("recruiter")

    q=request.GET.get("q","").strip()
    job_type=request.GET.get("type","")

    if q:
        qs=qs.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(skills_required__icontains=q) |
            Q(recruiter__company_name__icontains=q)
        )

    if job_type:
        qs=qs.filter(job_type=job_type)

    paginator=Paginator(qs,9)
    page=paginator.get_page(request.GET.get("page"))

    applied=set(
        Application.objects.filter(student=request.user)
        .values_list("job_id",flat=True)
    ) if request.user.is_authenticated and request.user.user_type=="student" else set()

    return render(
        request,
        "jobs/list.html",
        {
            "page":page,
            "applied":applied,
            "q":q,
            "job_type":job_type
        }
    )

def detail(request,job_id):
    job=get_object_or_404(Job.objects.select_related("recruiter","recruiter__user"),id=job_id)
    already=False
    if request.user.is_authenticated and request.user.user_type=="student": already=Application.objects.filter(job=job,student=request.user).exists()
    return render(request,"jobs/detail.html",{"job":job,"already":already})

@login_required
def create(request):
    if request.user.user_type!="recruiter": return redirect("jobs:list")
    profile,_=RecruiterProfile.objects.get_or_create(user=request.user,defaults={"company_name":request.user.username+" Company"})
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
            job=form.save(commit=False); job.recruiter=profile; job.save(); messages.success(request,"Opportunity posted successfully."); return redirect("recruiters:dashboard")
    else: form=JobForm()
    return render(request,"jobs/form.html",{"form":form,"heading":"Post an Opportunity"})

@login_required
def edit(request,job_id):
    job=get_object_or_404(Job, id=job_id, recruiter__user=request.user)
    if request.method=="POST":
        form=JobForm(request.POST,instance=job)
        if form.is_valid(): form.save(); messages.success(request,"Opportunity updated."); return redirect("recruiters:dashboard")
    else: form=JobForm(instance=job)
    return render(request,"jobs/form.html",{"form":form,"heading":"Edit Opportunity"})

@login_required
def apply(request, job_id):
    if request.user.user_type != "student":
        return redirect("jobs:detail", job_id=job_id)

    job = get_object_or_404(Job, id=job_id, is_active=True)

    # Check whether openings are available
    if job.openings <= 0:
        messages.error(request, "Applications are closed for this opportunity.")
        return redirect("jobs:detail", job_id=job_id)

    # Check deadline
    if job.deadline and job.deadline < timezone.localdate():
        messages.error(request, "The application deadline has passed.")
        return redirect("jobs:detail", job_id=job_id)

    # Check duplicate application
    if Application.objects.filter(job=job, student=request.user).exists():
        messages.info(request, "You have already applied for this opportunity.")
        return redirect("students:applications")

    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.student = request.user
            app.save()

            messages.success(
                request,
                "Application submitted successfully."
            )

            return redirect("students:applications")

    else:
        form = ApplicationForm()

    return render(
        request,
        "jobs/apply.html",
        {"job": job, "form": form}
    )

@login_required
def delete(request,job_id):
    job=get_object_or_404(Job,id=job_id,recruiter__user=request.user)
    if request.method=="POST": job.delete(); messages.success(request,"Opportunity deleted.")
    return redirect("recruiters:dashboard")
