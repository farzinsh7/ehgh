from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Houses(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    position = models.IntegerField(null=True)
    image = models.ImageField(upload_to='houses')
    banner = models.ImageField(upload_to="houses/banner", null=True)
    description = HTMLField()
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)

    def __str__(self):
        return self.title