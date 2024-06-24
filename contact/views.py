from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models
from . import forms


class ContactUsView(CreateView):
    model = models.ContactForm
    form_class = forms.ContactFormClass
    success_url = reverse_lazy('contact:page')
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = models.ContactUS.objects.first()
        return context