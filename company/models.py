from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Company(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='industry')
    image_thumbnail = models.ImageField(upload_to='industry/thumbs',
                            help_text=_('Best size: 684*489 PX'))
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)

    def __str__(self):
        return self.title
