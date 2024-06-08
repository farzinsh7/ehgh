from django.contrib import admin
from .models import Brands

# Register your models here.
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('thumbnail_tag', 'title', 'status')
    ordering = ['-created']

admin.site.register(Brands, BrandsAdmin)
