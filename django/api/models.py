from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    This is a generic base model, which other models below can inherit common fields from
    (e.g. admin and metadata fields)
    """
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')


class Project(BaseModel):
    """
    This model allows the users (and their journal entries) to be organised into different groups/projects.
    Each user can only belong to one project.
    """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    consent_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class JournalEntryTag(BaseModel):
    """
    This model allows journal entries to be categorised by tags,
    viewable and managable by end users (non-admin) on the client side.
    There are either public or user-specific tags (only viewable to the user that created it)
    as defined by the 'is_public' field
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    # Foreign key fields
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class JournalEntry(BaseModel):
    """
    This model is for recording end users' experiences
    """
    title = models.CharField(max_length=200)
    entry_text = models.TextField(blank=True, null=True)
    # Many to Many relationship fields
    journal_entry_tag = models.ManyToManyField(JournalEntryTag, blank=True)
    # Foreign key fields
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Journal entries"


class JournalEntryImage(BaseModel):
    """
    This model allows end users to upload multiple images for each journal entry
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='journalentryimages')
    # Foreign key fields
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.PROTECT)

    def __str__(self):
        return self.name if self.name is not None else str(self.image)


class JournalEntryAnalysisCode(BaseModel):
    """
    This model is for research teams to organise their journal entry analyses into multiple codes
    (like how tags work in JournalEntryTag for end users, but this is just for researchers/admins)
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class JournalEntryAnalysis(BaseModel):
    """
    This model is for research team to write comments and analysis (free text) about individual journal entries
    """
    analysis_text = models.TextField()
    # Foreign key fields
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    # Many to Many relationship fields
    journal_entry_analysis_code = models.ManyToManyField(JournalEntryAnalysisCode, blank=True)

    def __str__(self):
        if len(str(self.analysis_text)) > 27:
            return "{}...".format(str(self.analysis_text)[0:30])
        else:
            return self.analysis_text

    class Meta:
        verbose_name_plural = "Journal entry analyses"