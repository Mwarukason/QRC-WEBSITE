from django.conf.urls import url
from django.contrib import admin

#for django 1.10 above need to import
from .views import (post_create, post_detail,post_list,post_update,post_delete)

#from . import views

#importing app views
urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    #url(r'^qrcblog/$', "<appname>.views.<function_name>"),
]
