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

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractModel

'''
 This model used for holding ticket categories like:
 - New Features
 - Using Applications
 - Using APIs
 - Other
 '''
class Category(AbstractModel):
    class Meta:
        db_table = 'ot_category'
        verbose_name = _('Category')
    
    name = models.CharField(max_length=50, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class Department(AbstractModel):
    class Meta:
        db_table = 'ot_department'
    
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    active = models.BooleanField(verbose_name=_('Is Active'))

    def __str__(self):
        return self.name


class Organization(AbstractModel):
    class Meta:
        db_table = 'ot_organization'
    
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    active = models.BooleanField(verbose_name=_('Is Active'))

    def __str__(self):
        return self.name


class BlogPost(AbstractModel):
    class Meta:
        db_table = 'op_blogpost'
    
    name = models.CharField(max_length=256, verbose_name=_('Name'))
    body = models.TextField(verbose_name=_('Body'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Category'))

    def __str__(self):
        return self.name