from django import forms
from . import models


class ContactFormClass(forms.ModelForm):
    class Meta:
        model = models.ContactForm
        fields = ('name', 'email', 'message')
        widgets = {
        'name': forms.TextInput(attrs={'placeholder':'Your Name', 'type':'text', 'class':'fs-0 form-control','required':'required'}),
        'email': forms.EmailInput(attrs={'placeholder':'Email Address', 'type':'email', 'class':'fs-0 form-control','required':'required'}),
        'message': forms.Textarea(attrs={'placeholder':'Type your message here', 'class':'fs-0 form-control contact-message', 'row':'8','required':'required'}),
        }