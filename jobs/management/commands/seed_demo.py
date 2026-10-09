from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from recruiters.models import RecruiterProfile
from students.models import StudentProfile
from jobs.models import Job
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help="Create demo accounts and sample Career Hub opportunities"
    def handle(self,*args,**kwargs):
        User=get_user_model()
        student,_=User.objects.get_or_create(username="student_demo",defaults={"email":"student@example.com","user_type":"student"})
        student.user_type="student"; student.set_password("Student@123"); student.save()
        sp,_=StudentProfile.objects.get_or_create(user=student); sp.college="Aditya College of Engineering and Technology"; sp.degree="B.Tech"; sp.branch="CSE"; sp.graduation_year=2027; sp.skills="Python, Django, SQL, HTML, CSS, JavaScript"; sp.save()
        recruiter,_=User.objects.get_or_create(username="recruiter_demo",defaults={"email":"recruiter@example.com","user_type":"recruiter"})
        recruiter.user_type="recruiter"; recruiter.set_password("Recruiter@123"); recruiter.save()
        rp,_=RecruiterProfile.objects.get_or_create(user=recruiter,defaults={"company_name":"TechNova Solutions","industry":"Software","location":"Hyderabad","verified":True})
        rp.company_name="TechNova Solutions"; rp.verified=True; rp.save()
        samples=[("Python Django Intern","Build and maintain web applications with Django and Python.","Python, Django, SQL, HTML, CSS","internship","Hyderabad","₹20,000/month"),("Junior Software Engineer","Work with the engineering team to develop scalable applications.","Java, Python, SQL, Git","job","Bengaluru","₹6 LPA"),("Frontend Developer Referral","Referral opportunity for a frontend-focused developer.","HTML, CSS, JavaScript, React","referral","Remote","As per company policy")]
        for title,desc,skills,jt,loc,pay in samples:
            Job.objects.get_or_create(recruiter=rp,title=title,defaults={"description":desc,"skills_required":skills,"job_type":jt,"location":loc,"stipend_or_salary":pay,"openings":2,"deadline":timezone.localdate()+timedelta(days=30),"is_active":True})
        self.stdout.write(self.style.SUCCESS("Demo data created."))
        self.stdout.write("Student: student_demo / Student@123")
        self.stdout.write("Recruiter: recruiter_demo / Recruiter@123")
