# -*- coding: utf-8 -*-
from django.urls import path

from . import views

from tickets.app_views.pages.dashboard import dashboard
from tickets.app_views.api.analytics.chart import TicketHistoryData
from tickets.app_views.tickets.my_tickets import MyTickets

app_name = 'tickets'

urlpatterns = [
    path('', dashboard, name='home'),
    path('ticket/<int:id>', views.ticket, name='ticket'),

    path('user_profile/', views.user_profile, name='user_profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('submitter/<int:id>', views.submitter, name='submitter'),

    path('tickets/my_tickets/', MyTickets.as_view(), name='customer-my-tickets'),
    path('submit/', views.submit, name='submit'),

    path('api/analytics/ticket-history', TicketHistoryData.as_view(), name='api-analytics-history'),
    path('api/analytics/ticket-status', TicketHistoryData.as_view(), name='api-analytics-status'),
]
