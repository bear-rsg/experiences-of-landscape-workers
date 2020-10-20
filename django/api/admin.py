from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Experiences of Landscape Workers: Admin Dashboard'


class ProjectAdminView(admin.ModelAdmin):
    """
    Customise the Project section of the Django admin
    """
    list_display = ('name', 'description', 'admin_published', 'meta_lastupdated_datetime')
    list_filter = ('admin_published',)
    search_fields = ('name', 'description')
    ordering = ('-meta_lastupdated_datetime', 'name')


class JournalEntryAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry section of the Django admin
    """
    list_display = ('title', 'entry_text', 'project', 'user', 'admin_published', 'meta_lastupdated_datetime')
    list_filter = ('admin_published', 'project', 'user')
    search_fields = ('title', 'entry_text')
    ordering = ('-meta_lastupdated_datetime', 'title')


class JournalEntryImageAdminView(admin.ModelAdmin):
    """
    Customise the Journal Entry Images section of the Django admin
    """
    list_display = ('name', 'image', 'journal_entry', 'admin_published', 'meta_lastupdated_datetime')
    list_filter = ('admin_published',)
    search_fields = ('name',)
    ordering = ('-meta_lastupdated_datetime', 'name')


# Register classes
admin.site.register(models.Project, ProjectAdminView)
admin.site.register(models.JournalEntry, JournalEntryAdminView)
admin.site.register(models.JournalEntryImage, JournalEntryImageAdminView)
