from django.contrib import admin
from . import models

# Register your models here.
class TeamMemberAdmin(admin.TabularInline):
    model = models.TeamMember
    extra = 1
    max_num = 10


@admin.register(models.AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [TeamMemberAdmin]
