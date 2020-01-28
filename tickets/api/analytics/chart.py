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

from rest_framework.views import APIView
from rest_framework.response import Response

from utils import change_date2str

class TicketHistoryData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        data = {
              "type": "line",
              "data": {
                "labels": ["January","February","March","April","May","June","July"],
                "datasets": [{
                  "label": "No of submitted Tickets",
                  "data": [65, 59, 80, 81, 56, 55, 40, 25],
                  "fill": False,
                  "borderColor":"rgb(75, 192, 192)",
                  "lineTension":0.1}]
                },
              "options":{}
            }

        return Response(data)