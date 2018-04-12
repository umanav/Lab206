from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.users),
    url(r'^users/new$', views.add),
    url(r'^users/(?P<id>\d+)$', views.view_user),
    url(r'^users/(?P<id>\d+)/edit$', views.edit_user),
    url(r'^users/update$', views.update),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
]
