from django import forms
from core .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'full_name',
            'email',
            'phone_number',
            'message'
        ]
        labels = {
            'full_name': 'FULL NAME',
            'email': 'EMAIL ADDRESS',
            'phone_number': 'PHONE NUMBER',
            'message': 'MESSAGE'
        }
    
    