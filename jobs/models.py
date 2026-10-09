from django.db import models
from django.conf import settings
from recruiters.models import RecruiterProfile

class Job(models.Model):
    JOB_TYPES=(("internship","Internship"),("job","Full-time Job"),("referral","Referral"))
    recruiter=models.ForeignKey(RecruiterProfile,on_delete=models.CASCADE,related_name="jobs")
    title=models.CharField(max_length=200)
    description=models.TextField()
    skills_required=models.TextField(help_text="Comma-separated skills")
    job_type=models.CharField(max_length=20,choices=JOB_TYPES,default="internship")
    location=models.CharField(max_length=150,default="Remote")
    stipend_or_salary=models.CharField(max_length=100,blank=True)
    openings=models.PositiveIntegerField(default=1)
    deadline=models.DateField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: ordering=["-created_at"]
    def skill_list(self): return [s.strip().lower() for s in self.skills_required.split(",") if s.strip()]
    def __str__(self): return self.title

class Application(models.Model):
    STATUS_CHOICES=(("applied","Applied"),("review","Under Review"),("shortlisted","Shortlisted"),("interview","Interview"),("selected","Selected"),("rejected","Rejected"))
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name="applications")
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="applications")
    cover_note=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="applied")
    applied_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-applied_at"]
        constraints=[models.UniqueConstraint(fields=["job","student"],name="unique_job_student_application")]
    def __str__(self): return f"{self.student.username} - {self.job.title}"
