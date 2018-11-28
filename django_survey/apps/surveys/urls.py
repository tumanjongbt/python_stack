from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^survey/$', views.survey, name = "survey"),
    url(r'^result/$', views.result, name = "result"),
    url(r'^back/$', views.back, name = "back"),
]
