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

from django.contrib import admin

from .models import TicketCategory, Ticket, Comment


class TicketCategoryAmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)
    list_per_pages = 20

admin.site.register(TicketCategory, TicketCategoryAmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'organization', 'department', 'assigned_to', 'submitter', 'status', 'priority', 'starred')
    list_display_links = ('id', 'subject')
    list_filter = ('assigned_to', 'status', 'starred')
    list_editable = ('assigned_to', 'status', 'priority', 'starred')
    search_fields = ('id', 'subject', 'description', 'assigned_to', 'submitter', 'department', 'organization')
    fields = ('department', 'subject', 'description', 'assigned_to', 'submitter', 'organization', 'status', 'priority', 'starred', 'create_date', 'create_user', 'write_date', 'write_user')
    list_per_page = 20

admin.site.register(Ticket, TicketAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'note', 'ticket')
    search_fields = ('id', 'note', 'ticket')
    list_display_links = ('id', 'note')
    list_per_page = 20

admin.site.register(Comment, CommentAdmin)


