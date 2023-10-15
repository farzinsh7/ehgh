from django import forms
from .models import ContactForm


class ContactFormClass(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')
        widgets = {
        'name': forms.TextInput(attrs={'id': 'name', 'placeholder':'Name', 'type':'text'}),
        'email': forms.EmailInput(attrs={'id': 'email', 'placeholder':'Email', 'type':'email'}),
        'message': forms.Textarea(attrs={'id': 'message', 'placeholder':'Message'}),
        }