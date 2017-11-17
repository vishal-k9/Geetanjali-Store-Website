
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.product_detail, name='detail'),
]
