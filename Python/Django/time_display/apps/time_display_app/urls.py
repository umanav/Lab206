from django.conf.urls import url
from . import views          
print "urls.py Blogs"
urlpatterns = [
    url(r'^$', views.index),
]
