from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class JournalEntry(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    entry_text = models.TextField(blank=True, null=True)
    # Metadata fields
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    location = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JournalEntryImage(models.Model):
    id = models.IntegerField(primary_key=True)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='x')

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return str(self.image)
