from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tickets.models import Ticket

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