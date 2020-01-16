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