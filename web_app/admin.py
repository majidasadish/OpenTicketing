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
from datetime import datetime

from django.contrib import admin

from .models import Department, Organization, Category, BlogPost

class DepartmentAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('name', 'description', 'active')
    list_per_page = 20

admin.site.register(Department, DepartmentAmin)


class OrganizationAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('name', 'active')
    list_per_page = 20

admin.site.register(Organization, OrganizationAmin)


class CategoryAmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)
    list_per_pages = 20

admin.site.register(Category, CategoryAmin)


class BlogPostAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'create_date', 'create_user')
    fields = ('category', 'name', 'body')
    search_fields = ('name', 'category')
    list_display_links = ('id', 'name')
    list_per_pages = 20

    def save_model(self, request, obj, form, change):
        obj.create_user = request.user
        obj.save()


admin.site.register(BlogPost, BlogPostAmin)