from django.contrib import admin

from .models import Department, TicketCategory, Ticket, Comment


class DepartmentAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'active')
    search_fields = ('id', 'name')
    fields = ('name', 'description', 'active')
    list_per_page = 20

admin.site.register(Department, DepartmentAmin)


class TicketCategoryAmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)
    list_per_pages = 20

admin.site.register(TicketCategory, TicketCategoryAmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'department', 'assigned_to', 'submitter', 'status', 'priority', 'starred')
    list_display_links = ('id', 'subject')
    list_filter = ('assigned_to', 'status', 'starred')
    list_editable = ('assigned_to', 'status', 'priority', 'starred')
    search_fields = ('id', 'subject', 'description', 'assigned_to', 'submitter', 'department',)
    fields = ('department', 'subject', 'description', 'assigned_to', 'submitter', 'status', 'priority', 'starred', 'create_date', 'create_user', 'write_date', 'write_user')
    list_per_page = 20

admin.site.register(Ticket, TicketAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'note', 'ticket')
    search_fields = ('id', 'note', 'ticket')
    list_display_links = ('id', 'note')
    list_per_page = 20

admin.site.register(Comment, CommentAdmin)


