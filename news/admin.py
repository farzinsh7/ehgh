from django.contrib import admin
from . import models


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    autocomplete_fields = ["author"]
    prepopulated_fields = {"slug": ["title"]}
    list_display = ('title', 'status')
    list_filter = ('publish', 'status', 'category')
    search_fields = ('title', 'description')
    ordering = ['-publish']


admin.site.register(models.Category)
admin.site.register(models.Tags)