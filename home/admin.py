from django.contrib import admin
from . import models

# Register your models here.
class SocialLinksAdmin(admin.TabularInline):
    model = models.SocialLinks
    extra = 1
    max_num = 10


class HelpfulLinksAdmin(admin.TabularInline):
    model = models.HelpfulLinks
    extra = 1
    max_num = 10


class HelpfulLinks_2Admin(admin.TabularInline):
    model = models.HelpfulLinks_2
    extra = 1
    max_num = 10


@admin.register(models.SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    inlines = [SocialLinksAdmin, HelpfulLinksAdmin, HelpfulLinks_2Admin]
    


class SliderAdmin(admin.TabularInline):
    model = models.Slider
    extra = 1
    max_num = 3


class BrandsAdmin(admin.TabularInline):
    model = models.Brands
    extra = 1
    max_num = 6


class StatisticsAdmin(admin.TabularInline):
    model = models.Statistics
    extra = 1
    max_num = 3



@admin.register(models.HomeData)
class SiteInformationAdmin(admin.ModelAdmin):
    inlines = [SliderAdmin, BrandsAdmin, StatisticsAdmin]