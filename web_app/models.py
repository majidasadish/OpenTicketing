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
    