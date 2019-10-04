# -*- coding: utf-8 -*-
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

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
    return render(request, 'openticketing/client_my_tickets.html')

def submit(request):
    print(request.POST.get('department'))
    return render(request, 'openticketing/submit_ticket.html')

@login_required
def dashboard(request):
    #from django.apps.apps import get_model
    #t = get_model('openticketing', 'Ticket')
    my_tickets = Ticket.objects.filter(assigned_to__id=request.user.id).order_by('-create_date')
    form = TicketForm()
    return render(request, 'openticketing/dashboard.html', context=dict(tickets=my_tickets, form=form))

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
