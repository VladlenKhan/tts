from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_checked')

admin.site.register(Application, ApplicationAdmin)