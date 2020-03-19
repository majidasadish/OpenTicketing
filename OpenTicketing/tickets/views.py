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

from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Ticket
from .forms import TicketForm


@login_required
def user_settings(request):
    return HttpResponse('User settings page goes here!')

@login_required
def user_activity_log(request):
    return HttpResponse('User activities log goes here!')


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


def submitter(request, id):
    submitter = get_object_or_404(models.User, pk=id)
    return HttpResponse(f'submitter: {id} - {submitter}')
