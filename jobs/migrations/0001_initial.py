from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[('accounts','0001_initial'),('recruiters','0001_initial')]
    operations=[
        migrations.CreateModel(name='Job',fields=[
            ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
            ('title',models.CharField(max_length=200)),('description',models.TextField()),('skills_required',models.TextField(help_text='Comma-separated skills')),
            ('job_type',models.CharField(choices=[('internship','Internship'),('job','Full-time Job'),('referral','Referral')],default='internship',max_length=20)),
            ('location',models.CharField(default='Remote',max_length=150)),('stipend_or_salary',models.CharField(blank=True,max_length=100)),
            ('openings',models.PositiveIntegerField(default=1)),('deadline',models.DateField(blank=True,null=True)),('is_active',models.BooleanField(default=True)),
            ('created_at',models.DateTimeField(auto_now_add=True)),('updated_at',models.DateTimeField(auto_now=True)),
            ('recruiter',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='jobs',to='recruiters.recruiterprofile')),
        ],options={'ordering':['-created_at']}),
        migrations.CreateModel(name='Application',fields=[
            ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
            ('cover_note',models.TextField(blank=True)),('status',models.CharField(choices=[('applied','Applied'),('review','Under Review'),('shortlisted','Shortlisted'),('interview','Interview'),('selected','Selected'),('rejected','Rejected')],default='applied',max_length=20)),
            ('applied_at',models.DateTimeField(auto_now_add=True)),('updated_at',models.DateTimeField(auto_now=True)),
            ('job',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='applications',to='jobs.job')),
            ('student',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='applications',to=settings.AUTH_USER_MODEL)),
        ],options={'ordering':['-applied_at']}),
        migrations.AddConstraint(model_name='application',constraint=models.UniqueConstraint(fields=('job','student'),name='unique_job_student_application')),
    ]
