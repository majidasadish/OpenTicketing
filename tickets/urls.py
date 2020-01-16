# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('ticket/<int:id>', views.ticket, name='ticket'),

    path('user_profile/', views.user_profile, name='user_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submitter/<int:id>', views.submitter, name='submitter'),

    path('client_my_tickets/', views.client_my_tickets, name='client_my_tickets'),
    path('submit/', views.submit, name='submit'),

    path('api/data', views.get_chart_data, name='api-data'),
    path('api/chart/data', views.ChartData.as_view(), name='api-chart-data'),
]
