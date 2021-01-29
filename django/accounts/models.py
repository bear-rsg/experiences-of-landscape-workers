from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser_Title(models.Model):
    """
    Title for each custom user, e.g. Mr, Mrs, Dr, Prof.
    """

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class CustomUser_Project(models.Model):
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


class CustomUser(AbstractUser):
    """
    Custom user extends the standard Django user model, providing additional properties
    """

    title = models.ForeignKey(CustomUser_Title, on_delete=models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(CustomUser_Project, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
