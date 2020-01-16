# -*- coding: utf-8 -*-
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
def ticket(request, id):
    try:
        ticket = Ticket.objects.get(pk=id)
        return HttpResponse(f'my ticket - {id} : {ticket.subject}')
    except ObjectDoesNotExist:
        raise Http404("Ticket does not exists!")

def submitter(request, id):
    submitter = get_object_or_404(models.User, pk=id)
    return HttpResponse(f'submitter: {id} - {submitter}')
