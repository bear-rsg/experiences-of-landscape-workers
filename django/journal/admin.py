from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Experiences of Landscape Workers: Admin Dashboard'


class JournalEntryTagAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry Tag section of the Django admin
    """
    list_display = ('name', 'description', 'is_public', 'user', 'admin_published', 'meta_lastupdated_datetime')
    list_filter = ('admin_published', 'is_public', 'user')
    search_fields = ('name', 'description')
    ordering = ('-meta_lastupdated_datetime', 'name')


class JournalEntryAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry section of the Django admin
    """
    list_display = ('title', 'entry_text', 'entry_image', 'user', 'admin_published', 'meta_lastupdated_datetime')
    list_filter = ('admin_published', 'user')
    search_fields = ('title', 'entry_text')
    ordering = ('-meta_lastupdated_datetime', 'title')


class JournalEntryAnalysisCodeAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry Analysis Code section of the Django admin
    """
    list_display = ('name', 'description', 'admin_published', 'meta_lastupdated_datetime')
    list_filter = ('admin_published',)
    search_fields = ('name', 'description')
    ordering = ('-meta_lastupdated_datetime', 'name')


class JournalEntryAnalysisAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry Analysis section of the Django admin
    """
    list_display = ('analysis_text', 'journal_entry', 'admin_published', 'meta_lastupdated_datetime')
    list_filter = ('admin_published',)
    search_fields = ('analysis_text',)
    ordering = ('-meta_lastupdated_datetime', 'analysis_text')


# Register classes
admin.site.register(models.JournalEntryTag, JournalEntryTagAdminView)
admin.site.register(models.JournalEntry, JournalEntryAdminView)
admin.site.register(models.JournalEntryAnalysisCode, JournalEntryAnalysisCodeAdminView)
admin.site.register(models.JournalEntryAnalysis, JournalEntryAnalysisAdminView)
