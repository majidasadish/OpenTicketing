# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='openticketing/logout.html'), name='logout'),

]