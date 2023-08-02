from django.contrib import admin
from notification import models


@admin.register(models.Template)
class Templates(admin.ModelAdmin):

    search_fields = ['name']


@admin.register(models.Schedule)
class Schedules(admin.ModelAdmin):

    search_fields = ['name']


@admin.register(models.Configuration)
class Configs(admin.ModelAdmin):

    search_fields = ['name']

