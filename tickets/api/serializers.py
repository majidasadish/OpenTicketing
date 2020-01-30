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

from rest_framework import serializers

from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Ticket
        fields = [
            'url', 
            'pk', 
            'subject',
            'submitter', 
            #'category', 
            'create_user',
            'create_date', 
            'write_user', 
            'write_date',
        ]
        read_only_fields = ['pk', 'create_user', 'create_date', 'write_user', 'write_date',]

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

    # convert to JSON
    # validation for data passed
    def validate_subject(self, value):
        print('validate subject field for %s!' % value)
        qs = Ticket.objects.filter(subject__iexact=value)
        if self.instance.pk:
            qs = qs.exclude(id=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('The subject must be exact!')
        else:
            return value