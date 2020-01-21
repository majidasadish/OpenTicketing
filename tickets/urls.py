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

from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

from tickets.app_views.pages.dashboard import dashboard
from tickets.app_views.api.analytics.chart import TicketHistoryData
from tickets.app_views.tickets.my_tickets import MyTickets
from tickets.app_views.tickets.ticket import TicketView


app_name = 'tickets'

urlpatterns = [
    path('', dashboard, name='home'),
    path('ticket/<int:id>', login_required(TicketView.as_view()), name='ticket'),

    path('dashboard/', dashboard, name='dashboard'),
    path('submitter/<int:id>', views.submitter, name='submitter'),

    path('tickets/my_tickets/', MyTickets.as_view(), name='customer-my-tickets'),
    path('submit/', views.submit, name='submit'),

    path('api/analytics/ticket-history', TicketHistoryData.as_view(), name='api-analytics-history'),
    path('api/analytics/ticket-status', TicketHistoryData.as_view(), name='api-analytics-status'),
]
