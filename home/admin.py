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


@admin.register(models.SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    inlines = [SocialLinksAdmin, HelpfulLinksAdmin]