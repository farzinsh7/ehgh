from django.contrib import admin
from .models import Industry

# Register your models here.
class IndustryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Industry, IndustryAdmin)