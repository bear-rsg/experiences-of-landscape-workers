from django.contrib import admin
from . import models


class ProjectAdminView(admin.ModelAdmin):
    """
    Customise the Project section of the Django admin
    """
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class JournalEntryAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry section of the Django admin
    """
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


class JournalEntryImageAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry Images section of the Django admin
    """
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


# Register classes
admin.site.register(models.Project, ProjectAdminView)
admin.site.register(models.JournalEntry, JournalEntryAdminView)
admin.site.register(models.JournalEntryImage, JournalEntryImageAdminView)
