from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class JournalEntry(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    entry_text = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JournalEntryImage(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='journalentryimages')
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True)
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return str(self.image)
