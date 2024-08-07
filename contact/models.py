from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactUS(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to="contact/banner", null=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200)
    iframe = models.TextField()

    def __str__(self):
        return self.title