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

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractModel
from web_app.models import Department, Organization

'''
 This model used for holding ticket categories like:
 - New Features
 - Using Applications
 - Using APIs
 - Other
 '''
class TicketCategory(AbstractModel):
    class Meta:
        db_table = 'ot_category'
        verbose_name = _('Ticket category')
    
    name = models.CharField(max_length=50, verbose_name=_('Name'))

    def __str__(self):
        return self.name
    

class Ticket(AbstractModel):
    class Meta:
        db_table = 'ot_ticket'

    PRIORITIES = [
        (1, _('High')),
        (2, _('Normal')),
        (3, _('Low')),
    ]
    
    STATUS = [
        (1, _('Draft')),
        (2, _('Open')),
        (3, _('Closed')),
        (4, _('Pending')),
    ]

    subject = models.CharField(max_length=200, verbose_name=_('Subject'))
    description = models.TextField(verbose_name=_('Description'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Department'))
    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Help Topics'))
    submitter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submitter_uid',
        blank=True,
        null=True,
        verbose_name=_('Submitter'),
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Organization'))
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_uid',
        blank=True,
        null=True,
        verbose_name=_('Assigned to'),
    )
    priority = models.IntegerField(verbose_name=_('Priority'), choices=PRIORITIES, default=2)
    status = models.IntegerField(verbose_name=_('Status'), choices=STATUS, default=1)
    starred = models.BooleanField(verbose_name=_('Starred'), default=False)
    dependencies = models.ManyToManyField("self", blank=True)

    def get_comments(self):
        if self.comments.count():
            return self.comments.order_by('-create_date')

    def __str__(self):
        return f"{self.subject} [{self.submitter}]"


class TicketAttachments(AbstractModel):
    class Meta:
        db_table = 'ot_ticket_attachments'
    
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='attachments',
        blank=True,
        null=True,
        verbose_name=_('Ticket')
    )
    doc_file = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.name

class Comment(AbstractModel):
    class Meta:
        db_table = 'ot_comment'

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name=_('Ticket')
    )
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    note = models.TextField(verbose_name=_('Note'))