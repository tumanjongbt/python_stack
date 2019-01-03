from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name ="dashboard"),
    url(r'^addjob$', views.addjob, name = "addjob"),
    url(r'^create$', views.create, name = "create"),
    url(r'^myjobs/(?P<job_id>\d+)$', views.myjobs, name ="myjobs"),
    url(r'^view/(?P<job_id>\d+)$', views.view, name = "view"),
    url(r'^edit/(?P<job_id>\d+)$', views.edit, name = "edit"),
    url(r'^update/(?P<job_id>\d+)$', views.update, name = "update"),
    url(r'^delete/(?P<job_id>\d+)$', views.delete, name = "delete"),
]
