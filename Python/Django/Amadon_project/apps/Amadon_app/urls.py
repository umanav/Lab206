from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/buy$', views.purchase),
    url(r'^checkout$', views.checkout),
    
]
