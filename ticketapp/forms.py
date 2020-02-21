from django import forms
from .models import Complain,Ticket

class ComplainForm(forms.ModelForm):
    class Meta():
        model=Complain
        fields=['subject','complain','image']

        widgets={
            'subject':forms.TextInput(attrs={'placeholder':"Subject", "class":"form-control"}),
             'image':forms.FileInput(attrs={'class':"form-control"}),
             'complain':forms.Textarea(attrs={"class":'form-control','rows':2})
        }
        
class TicketForm(forms.ModelForm):
    class Meta():
        model=Ticket
        fields=[]
