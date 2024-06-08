from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.utils.html import format_html

# Create your models here.
class Brands(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    description = HTMLField()
    founded = models.DateTimeField(default=timezone.now)
    line = models.CharField(max_length=300,blank=True,null=True)
    website = models.CharField(max_length=300,blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    image = models.ImageField(upload_to='brands')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)

    def __str__(self):
        return self.title
    

    def thumbnail_tag(self):
        return format_html(
            "<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.image.url))
        

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='slider')
    home_data = models.ForeignKey(Brands, null=True, on_delete=models.SET_NULL, related_name='sliders')

    def __str__(self):
        return self.title
    

class SocialLinks(models.Model):
    label = models.CharField(max_length=120, null=True)
    icon = models.CharField(null=True, max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(Brands, null=True, on_delete=models.SET_NULL, related_name='socials')

    def __str__(self):
        return self.label if self.label else "No Label"