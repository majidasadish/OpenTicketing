from django.core.paginator import Paginator
from django.views.generic.base import TemplateView


from tickets.models import Ticket

class MyTickets(TemplateView):
    template_name = 'openticketing/tickets/my_tickets.html'

    def get_context_data(self, **kwargs):
        open_ticket_listings = Ticket.objects.filter(status=2).order_by('-create_date')
        paginator = Paginator(open_ticket_listings, 20)
        page = self.request.GET.get('page')
        paged_open_tickets = paginator.get_page(page)

        context = super().get_context_data(**kwargs)
        context.update(open_tickets=paged_open_tickets)
        return context
