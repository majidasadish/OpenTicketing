
from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['department', 'category', 'subject', 'description', 'priority']

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'placeholder' : 'Please enter a brief summary here'})
        self.fields['subject'].label = ''
        self.fields['description'].widget.attrs.update({'placeholder' : 'Please describe the ticket in more details'})
        self.fields['description'].label = ''
        


