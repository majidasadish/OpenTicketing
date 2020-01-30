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

from datetime import datetime

from django.db.models import Q

from rest_framework import generics, mixins, permissions

from tickets.models import Ticket
from .permissions import IsOwner
from .serializers import TicketSerializer

class TicketListView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = TicketSerializer
    # queryset = Ticket.objects.all()

    def get_queryset(self):
        qs = Ticket.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                        Q(subject__icontains=query)|
                        Q(description__icontains=query)
                        ).distinct()
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
        
    def perform_create(self, serializer):
        serializer.save(create_user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    #def put(self, request, *args, **kwargs):
    #    self.update(request, *args, **kwargs)

    #def patch(self, request, *args, **kwargs):
    #    self.update(request, *args, **kwargs)


class TicketRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = TicketSerializer
    # permission_classes = [permissions.IsAuthenticated, IsOwner]
    # queryset = Ticket.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def get_queryset(self):
        return Ticket.objects.all()
    
    def get_object(self):
        pk = self.kwargs.get('id')
        return Ticket.objects.get(pk=pk)

    #def perform_update(self, serializer):
    #    serializer.save(write_user=None, write_date=datetime.now())#self.request.user
    
    
