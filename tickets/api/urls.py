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

from django.conf.urls import url
from django.urls import path

from .analytics.chart import TicketHistoryData
from .ticket import TicketRUDView, TicketListView

urlpatterns = [
    path('api/analytics/ticket-history', TicketHistoryData.as_view(), name='api-analytics-history'),
    path('api/analytics/ticket-status', TicketHistoryData.as_view(), name='api-analytics-status'),

    # Example: http://127.0.0.1:8000/tickets/api/1/
    url(r'^(?P<id>\d+)/$', TicketRUDView.as_view(), name='ticket-api'),
    path('', TicketListView.as_view(), name='ticket-create'),
]