from django.contrib import admin
from . import models

class SocialLinksAdmin(admin.TabularInline):
    model = models.SocialLinks
    extra = 1
    max_num = 10


class SliderAdmin(admin.TabularInline):
    model = models.Slider
    extra = 1
    max_num = 10


@admin.register(models.Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('thumbnail_tag', 'title', 'status')
    search_fields = ('title', 'description')
    inlines = [SliderAdmin, SocialLinksAdmin]
    ordering = ['-created']


# admin.site.register(models.Tags)
