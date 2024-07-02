from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class HomeData(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=300, null=True)
    header_img = models.ImageField(upload_to='home/header', null=True)
    header_img_mobile = models.ImageField(upload_to='home/header', null=True)
    about_img = models.ImageField(upload_to='home/banner')
    about = HTMLField(null=True)
    about2 = HTMLField(null=True)
    video = models.FileField(upload_to="home/video", blank=True,null=True)
    video_banner = models.ImageField(upload_to='home/banner', null=True)
    video_banner_mobile = models.ImageField(upload_to='home/banner', null=True)
    statistics_banner = models.ImageField(upload_to='home/banner', null=True)
    statistics_banner_mobile = models.ImageField(upload_to='home/banner', null=True)

    def __str__(self):
        return self.title


class Statistics(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='home/icons', blank=True, null=True)
    data = models.IntegerField(null=True)
    home_data = models.ForeignKey(HomeData, null=True, on_delete=models.SET_NULL, related_name='statistics')

    def __str__(self):
        return self.title


class SiteInformation(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo', null=True)
    mission = models.TextField(null=True)
    vision = models.TextField(null=True)
    value = models.TextField(null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.title
    
    
class SocialLinks(models.Model):
    label = models.CharField(max_length=120, null=True)
    icon = models.CharField(null=True, max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(SiteInformation, null=True, on_delete=models.SET_NULL, related_name='socials')

    def __str__(self):
        return self.label if self.label else "No Label"
    


class HelpfulLinks(models.Model):
    title = models.CharField(max_length=120, null=True)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(SiteInformation, null=True, on_delete=models.SET_NULL, related_name='links')

    def __str__(self):
        return self.title if self.title else "No Title"
    

class HelpfulLinks_2(models.Model):
    title = models.CharField(max_length=120, null=True)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(SiteInformation, null=True, on_delete=models.SET_NULL, related_name='links2')

    def __str__(self):
        return self.title if self.title else "No Title"