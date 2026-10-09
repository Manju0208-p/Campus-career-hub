from django.urls import path
from . import views
app_name="students"
urlpatterns=[path("profile/",views.profile,name="profile"),path("applications/",views.applications,name="applications"),path("recommendations/",views.recommendations,name="recommendations")]
