from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.ninjagame.urls', namespace="ninjagame")),
]
 #ticket app is the root app for projects