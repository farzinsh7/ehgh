from django.db import models


# Create your models here.
class SiteInformation(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo', null=True)
    description = models.TextField(null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=300, null=True)
    instagram = models.URLField(null=True)
    telegram = models.URLField(null=True)
    whatsapp = models.URLField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.title