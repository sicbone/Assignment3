from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from django.views.generic import DetailView
from mcdelivery import views
from mcdelivery.models import Order

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^listall/$', views.OrderList.as_view()),
    url(r'^add/$', views.OrderCreate.as_view(), name='order_add'),
    url(r'^orders/(?P<pk>\d+)$', views.OrderDetail.as_view(), name='detail'),
    url(r'^orders/(?P<pk>\d+)/edit/$', views.OrderUpdate.as_view(),  name='order_update'),
    url(r'^orders/(?P<pk>\d+)/delete/$', views.OrderDelete.as_view(), name='delete')
)