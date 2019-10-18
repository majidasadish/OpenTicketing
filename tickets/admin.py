from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'assigned_to', 'submitter', 'priority', 'starred')
    fields = ['subject', 'description', 'assigned_to', 'submitter', 'priority', 'starred', 'create_date', 'create_user', 'write_date', 'write_user']


admin.site.register(Ticket, TicketAdmin)


