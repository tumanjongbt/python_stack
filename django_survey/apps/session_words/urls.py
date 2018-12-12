from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^new/$', views.new, name="new"),
    url(r'^create/$', views.create, name="create"),
    url(r'^clear/$', views.clear, name="clear"),
]