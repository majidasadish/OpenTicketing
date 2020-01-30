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

from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from tickets.models import Ticket

User = get_user_model()

class TicketTestCase(APITestCase):

    def setUp(self):
        user_obj = User(username="test", email="test@openticketing.org")
        user_obj.set_password("someRandomPassword123")
        user_obj.save()
        ticket_obj = Ticket.objects.create(
            subject="New Subject", 
            description="some description",
            submitter=user_obj)

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_ticket(self):
        ticket_count = Ticket.objects.count()
        self.assertEqual(ticket_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse('tickets:ticket-api:listcreate')
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_ticket(self):
        ticket = Ticket.objects.first()
        data = {"subject":"new subject!"}
        url = ticket.get_api_url()
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)