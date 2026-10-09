from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[('accounts','0001_initial')]
    operations=[migrations.CreateModel(name='RecruiterProfile',fields=[
        ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
        ('company_name',models.CharField(max_length=200)),('company_website',models.URLField(blank=True)),
        ('company_description',models.TextField(blank=True)),('industry',models.CharField(blank=True,max_length=150)),
        ('location',models.CharField(blank=True,max_length=150)),('phone',models.CharField(blank=True,max_length=20)),
        ('verified',models.BooleanField(default=False)),
        ('user',models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,related_name='recruiter_profile',to=settings.AUTH_USER_MODEL)),
    ])]
