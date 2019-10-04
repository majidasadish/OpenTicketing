# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.views import LoginView, redirect_to_login
from django.shortcuts import render, resolve_url

default_login_view = LoginView.as_view(template_name='openticketing/login.html')

def home(request):
    return render(request, 'openticketing/home.html')

def login(request):
    # Prevent redirect loop by checking that LOGIN_URL is not this view's name
    if settings.LOGIN_URL and settings.LOGIN_URL != request.resolver_match.view_name:
        next_url = 'next' in request.GET and request.GET['next'] or resolve_url('home')
        return redirect_to_login(next_url, settings.LOGIN_URL)
    else:
        return default_login_view(request)