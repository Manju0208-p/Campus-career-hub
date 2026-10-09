from django.urls import path
from . import views
app_name="jobs"
urlpatterns=[path("",views.jobs_list,name="list"),path("<int:job_id>/",views.detail,name="detail"),path("create/",views.create,name="create"),path("<int:job_id>/edit/",views.edit,name="edit"),path("<int:job_id>/apply/",views.apply,name="apply"),path("<int:job_id>/delete/",views.delete,name="delete")]
