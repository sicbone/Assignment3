from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^login/$', login, {'template_name':'accounts/login.html'},name='login'), 
    url(r'^logout/$', logout, {'next_page':'/home'}, name='logout'), 
    url(r'^register/$', 'accounts.views.registration', name='register'),
)