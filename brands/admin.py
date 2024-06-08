from django.contrib import admin
from .models import Brands, SocialLinks, Slider, Tags, Line

class SocialLinksAdmin(admin.TabularInline):
    model = SocialLinks
    extra = 1
    max_num = 10


class SliderAdmin(admin.TabularInline):
    model = Slider
    extra = 1
    max_num = 10


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('thumbnail_tag', 'title', 'status')
    search_fields = ('title', 'description')
    inlines = [SliderAdmin, SocialLinksAdmin]
    ordering = ['-created']
    


admin.site.register(Line)
admin.site.register(Tags)
