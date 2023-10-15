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
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    google_map = models.URLField(null=True)

    def __str__(self):
        return self.title