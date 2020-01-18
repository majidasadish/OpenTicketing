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

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.views.generic.base import TemplateView

from tickets.models import Ticket

class TicketView(TemplateView):
    template_name = 'openticketing/tickets/ticket.html'

    def get_context_data(self, **kwargs):
        try:
            ticket = Ticket.objects.get(pk=kwargs.get('id'))
        except ObjectDoesNotExist:
            raise Http404("Ticket does not exists!")
        context = super().get_context_data(**kwargs)
        context.update(ticket=ticket)
        return context