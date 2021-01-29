from django.contrib.auth.models import AbstractUser
from django.db import models


class Title(models.Model):
    """
    Title for each custom user, e.g. Mr, Mrs, Dr, Prof.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    This model allows the users (and their journal entries) to be organised into different groups/projects.
    Each user can only belong to one project.
    """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    consent_message = models.TextField(blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    """
    Custom user extends the standard Django user model, providing additional properties
    """
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
