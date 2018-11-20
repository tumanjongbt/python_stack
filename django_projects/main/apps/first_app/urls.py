from django.conf.urls import url # gives access to the function url
from . import views # imports views.py in the current folder
urlpatterns = [
    url(r'^$', views.index)
]

# r tells python to interpret the following as a raw string, so it won't escape any special characters
# In this case the regex will exactly match an empty string (r'^$'), and matches the pattern views.index