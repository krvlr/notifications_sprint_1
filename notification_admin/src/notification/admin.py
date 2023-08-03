from django.contrib import admin
from notification import models


@admin.register(models.Template)
class Templates(admin.ModelAdmin):

    search_fields = ['name', 'description', 'id']


@admin.register(models.Schedule)
class Schedules(admin.ModelAdmin):

    search_fields = ['name', 'description', 'id']


@admin.register(models.Configuration)
class Configs(admin.ModelAdmin):

    search_fields = ['name', 'description', 'id']
