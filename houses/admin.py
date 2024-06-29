from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Houses)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['position']