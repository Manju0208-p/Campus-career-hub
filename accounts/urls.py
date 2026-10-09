from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import CareerLoginView, register, profile, edit_account

app_name="accounts"
urlpatterns=[
    path("login/",CareerLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("register/",register,name="register"),
    path("profile/",profile,name="profile"),
    path("profile/edit/",edit_account,name="edit_account"),
]
