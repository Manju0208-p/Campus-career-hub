from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets=UserAdmin.fieldsets+(("Career Hub",{"fields":("user_type",)}),)
    add_fieldsets=UserAdmin.add_fieldsets+(("Career Hub",{"fields":("email","user_type")}),)
    list_display=("username","email","user_type","is_staff","is_active")
    list_filter=("user_type","is_staff","is_active")
