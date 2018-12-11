from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^create/$', views.create, name="create"),
    url(r'^clear/$', views.clear, name="clear"),


]