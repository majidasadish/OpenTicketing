from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(default=datetime.now)
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_create_uid',
        blank=True,
        null=True,
        verbose_name=_('Created by'),
        )
    write_date = models.DateTimeField(
        blank=True, 
        null=True,
        verbose_name=_('Last modified'))
    write_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_write_uid',
        blank=True,
        null=True,
        verbose_name=_('Last modified by'),
        )
    

class Ticket(AbstractModel):
    class Meta:
        db_table = 'openticketing_ticket'

    PRIORITIES = [
        (1, _('High')),
        (2, _('Normal')),
        (3, _('Low')),
    ]
    
    subject = models.CharField(max_length=200, verbose_name=_('Subject'))
    description = models.TextField(verbose_name=_('Description'))
    submitter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submitter_uid',
        blank=True,
        null=True,
        verbose_name=_('Submitter'),
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_uid',
        blank=True,
        null=True,
        verbose_name=_('Assigned to'),
    )
    priority = models.IntegerField(verbose_name=_('Priority'), choices=PRIORITIES, default=2)
    starred = models.BooleanField(verbose_name=_('Starred'), default=False)

    def __str__(self):
        return f"{self.subject} [{self.submitter}]"


class Comment(AbstractModel):
    note = models.TextField(verbose_name=_('Note'))
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name=_('Comment')
    )