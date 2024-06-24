from django import forms
from . import models


class ContactFormClass(forms.ModelForm):
    class Meta:
        model = models.ContactForm
        fields = ('name', 'email', 'message', 'captcha')
        widgets = {
        'name': forms.TextInput(attrs={'id': 'name', 'placeholder':'Name', 'type':'text'}),
        'email': forms.EmailInput(attrs={'id': 'email', 'placeholder':'Email', 'type':'email'}),
        'message': forms.Textarea(attrs={'id': 'message', 'placeholder':'Message'}),
        }