# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenTicketing, 
#    Copyright (C) 2019-2020 OpenTicketing (<https://github.com/loghmanb/OpenTicketing>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from django.conf import settings
from django.contrib.auth.views import LoginView, redirect_to_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, resolve_url

from .models import BlogPost

default_login_view = LoginView.as_view(template_name='openticketing/login.html')

def home(request):
    blog_posts = BlogPost.objects.order_by('-create_date')[:6]
    return render(request, 'openticketing/home.html', context=dict(blog_posts= blog_posts))

def login(request):
    # Prevent redirect loop by checking that LOGIN_URL is not this view's name
    if settings.LOGIN_URL and settings.LOGIN_URL != request.resolver_match.view_name:
        next_url = 'next' in request.GET and request.GET['next'] or resolve_url('home')
        return redirect_to_login(next_url, settings.LOGIN_URL)
    else:
        return default_login_view(request)

@login_required
def user_profile(request):
    return render(request, 'openticketing/web_app/user_profile.html')

@login_required
def user_setting(request):
    return render(request, 'openticketing/web_app/user_settings.html')