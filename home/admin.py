from django.contrib import admin
from .models import SiteInformation, SocialLinks


class SocialLinksAdmin(admin.TabularInline):
    model = SocialLinks
    extra = 1
    max_num = 10


@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    inlines = [SocialLinksAdmin]