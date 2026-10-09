from django.conf import settings
from django.db import models

class StudentProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="student_profile")
    college=models.CharField(max_length=200,blank=True)
    degree=models.CharField(max_length=150,blank=True)
    branch=models.CharField(max_length=150,blank=True)
    graduation_year=models.PositiveIntegerField(null=True,blank=True)
    phone=models.CharField(max_length=20,blank=True)
    skills=models.TextField(blank=True,help_text="Comma-separated skills")
    bio=models.TextField(blank=True)
    resume=models.FileField(upload_to="resumes/",blank=True,null=True)
    linkedin=models.URLField(blank=True)
    github=models.URLField(blank=True)
    updated_at=models.DateTimeField(auto_now=True)

    def skill_list(self): return [s.strip().lower() for s in self.skills.split(",") if s.strip()]
    def __str__(self): return self.user.get_full_name() or self.user.username
