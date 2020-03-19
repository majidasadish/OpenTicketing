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

from django.core.paginator import Paginator
from django.views.generic.base import TemplateView


from tickets.models import Ticket

class MyTickets(TemplateView):
    template_name = 'openticketing/tickets/my_tickets.html'

    def get_context_data(self, **kwargs):
        open_ticket_listings = Ticket.objects.filter(status=2).order_by('-create_date')
        paginator = Paginator(open_ticket_listings, 20)
        page = self.request.GET.get('page')
        paged_open_tickets = paginator.get_page(page)

        context = super().get_context_data(**kwargs)
        context.update(open_tickets=paged_open_tickets)
        return context
