from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class AboutCompany(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="about")
    banner = models.ImageField(upload_to="about/banner", null=True)
    description = HTMLField()
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=300, null=True)
    position = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to="about/members", null=True)
    about = models.ForeignKey(AboutCompany, null=True, on_delete=models.SET_NULL, related_name='members')
    
    def __str__(self):
        return self.name