from django.conf.urls import patterns, include, url
from django.contrib import admin
from mcdelivery import views

urlpatterns = patterns('',
    # url(r'/'),
    url(r'^orders/(?P<order_id>\d+)$', views.order, name='detail'),
    url(r'^orders/$', views.order_list, name='order_list'),
    url(r'^admin/', include(admin.site.urls)),
)