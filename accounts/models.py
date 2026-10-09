from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES=( ("student","Student"), ("recruiter","Recruiter") )
    user_type=models.CharField(max_length=20, choices=USER_TYPES)
    email=models.EmailField(unique=True)
    REQUIRED_FIELDS=["email","user_type"]

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
