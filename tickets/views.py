# -*- coding: utf-8 -*-
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Ticket
from .forms import TicketForm

@login_required
def user_profile(request):
    return HttpResponse('Profile page goes here!')

@login_required
def user_settings(request):
    return HttpResponse('User settings page goes here!')

@login_required
def user_activity_log(request):
    return HttpResponse('User activities log goes here!')

def client_my_tickets(request):
    open_ticket_listings = Ticket.objects.filter(status=2).order_by('-create_date')
    paginator = Paginator(open_ticket_listings, 20)
    page = request.GET.get('page')
    paged_open_tickets = paginator.get_page(page)
    return render(request, 'openticketing/client_my_tickets.html', context=dict(open_tickets=paged_open_tickets))

@login_required
def submit(request):
    is_ticket_submitted = False
    ticket_id = None
    message = ''
    if request.method=='POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            is_ticket_submitted = True
            ticket_id = ticket.id
            message = f"'{request.POST['subject']}' is submitted succesfuly!"
    else:
        form = TicketForm()
    return render(request, 'openticketing/submit_ticket.html', 
                  context=dict(form=form, is_ticket_submitted=is_ticket_submitted, ticket_id=ticket_id, message=message))

@login_required
def dashboard(request):
    #from django.apps.apps import get_model
    #t = get_model('openticketing', 'Ticket')
    from django.db import connection
    with connection.cursor() as cr:
        cr.execute("select count(id) no_of_items, strftime('%Y-%m', create_date) [month] "
                    "from openticketing_ticket group by strftime('%Y-%m', create_date) "
                    "order by strftime('%Y-%m', create_date) desc limit 10 offset 0")
        rows = cr.fetchall()
        print(rows)
    my_tickets = Ticket.objects.filter(assigned_to__id=request.user.id).order_by('-create_date')
    return render(request, 'openticketing/dashboard.html', context=dict(tickets=my_tickets))

def get_chart_data(request, *args, **kwargs):
    return JsonResponse({'sales':100, 'customers':10})

from rest_framework.views import APIView
from rest_framework.response import Response
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        return Response({'sales':100, 'customers':10})

@login_required
def ticket(request, id):
    try:
        ticket = Ticket.objects.get(pk=id)
        return HttpResponse(f'my ticket - {id} : {ticket.subject}')
    except ObjectDoesNotExist:
        raise Http404("Ticket does not exists!")

def submitter(request, id):
    submitter = get_object_or_404(models.User, pk=id)
    return HttpResponse(f'submitter: {id} - {submitter}')
