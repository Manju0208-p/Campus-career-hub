from django.urls import path
from . import views
app_name="recruiters"
urlpatterns=[path("profile/",views.profile,name="profile"),path("dashboard/",views.dashboard,name="dashboard"),path("jobs/<int:job_id>/applicants/",views.applicants,name="applicants"),path("applications/<int:application_id>/status/",views.update_application,name="update_application")]
