from django.contrib import admin
from .models import SiteInformation, SocialLinks, Slider, Features, HomeData, NewsLetter


class SocialLinksAdmin(admin.TabularInline):
    model = SocialLinks
    extra = 1
    max_num = 10


@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    inlines = [SocialLinksAdmin]


class SliderAdmin(admin.TabularInline):
    model = Slider
    extra = 1
    max_num = 10

class FeaturesAdmin(admin.TabularInline):
    model = Features
    extra = 1
    max_num = 3


@admin.register(HomeData)
class SiteInformationAdmin(admin.ModelAdmin):
    inlines = [SliderAdmin, FeaturesAdmin]


admin.site.register(NewsLetter)