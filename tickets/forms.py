
from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'description', 'priority']

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        #self.fields['myfield'].widget.attrs.update({'class' : 'myfieldclass'})


