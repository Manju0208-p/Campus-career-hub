from django.conf import settings
from django.db import models

class RecruiterProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="recruiter_profile")
    company_name=models.CharField(max_length=200)
    company_website=models.URLField(blank=True)
    company_description=models.TextField(blank=True)
    industry=models.CharField(max_length=150,blank=True)
    location=models.CharField(max_length=150,blank=True)
    phone=models.CharField(max_length=20,blank=True)
    verified=models.BooleanField(default=False)
    def __str__(self): return self.company_name
