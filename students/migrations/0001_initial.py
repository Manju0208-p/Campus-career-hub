from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[('accounts','0001_initial')]
    operations=[migrations.CreateModel(name='StudentProfile',fields=[
        ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
        ('college',models.CharField(blank=True,max_length=200)),('degree',models.CharField(blank=True,max_length=150)),
        ('branch',models.CharField(blank=True,max_length=150)),('graduation_year',models.PositiveIntegerField(blank=True,null=True)),
        ('phone',models.CharField(blank=True,max_length=20)),('skills',models.TextField(blank=True,help_text='Comma-separated skills')),
        ('bio',models.TextField(blank=True)),('resume',models.FileField(blank=True,null=True,upload_to='resumes/')),
        ('linkedin',models.URLField(blank=True)),('github',models.URLField(blank=True)),('updated_at',models.DateTimeField(auto_now=True)),
        ('user',models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,related_name='student_profile',to=settings.AUTH_USER_MODEL)),
    ])]
