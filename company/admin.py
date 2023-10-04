from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Company, CompanyAdmin)
