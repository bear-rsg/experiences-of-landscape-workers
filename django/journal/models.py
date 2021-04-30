from django.db import models
from django.urls import reverse
from django.conf import settings
from PIL import Image, ImageOps


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class JournalEntry(BaseModel):
    """
    This model is for recording end users' experiences
    """
    title = models.DateTimeField(auto_now_add=True)
    entry_text = models.TextField()
    entry_image = models.ImageField(upload_to='journalentryimages', blank=True, null=True)
    # Many to Many relationship fields
    journal_entry_tag = models.ManyToManyField(JournalEntryTag, blank=True)
    # Foreign key fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('journal-journalentry-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        """
        Override save method to reduce quality of photos, to improve performance
        """
        super().save(*args, **kwargs)

        if self.entry_image:
            img = Image.open(self.entry_image.path)
            img = ImageOps.exif_transpose(img)
            img.save(self.entry_image.path, quality=40, optimize=True)

    class Meta:
        verbose_name_plural = "Journal entries"


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    # Many to Many relationship fields
    journal_entry_analysis_code = models.ManyToManyField(JournalEntryAnalysisCode, blank=True)

    def __str__(self):
        if len(str(self.analysis_text)) > 27:
            return "{}...".format(str(self.analysis_text)[0:30])
        else:
            return self.analysis_text

    class Meta:
        verbose_name_plural = "Journal entry analyses"
