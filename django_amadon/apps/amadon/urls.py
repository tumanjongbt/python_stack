# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$/', views.index, name="index"),
#     url(r'^buy$/', views.buy, name = "buy"),
#     url(r'^checkout$/', views.checkout, name = "checkout"),
# ]

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^buy/$', views.buy, name="buy"),
	url(r'^checkout/$', views.checkout, name="checkout"),

]