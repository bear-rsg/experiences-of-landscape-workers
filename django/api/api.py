from . import models, serializers
from rest_framework import viewsets, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Project model
    """

    queryset = models.Project.objects.filter(admin_published=True)
    serializer_class = serializers.ProjectSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class JournalEntryTagViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry Tag model
    """

    queryset = models.JournalEntryTag.objects.filter(admin_published=True)
    serializer_class = serializers.JournalEntryTagSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry model
    """

    queryset = models.JournalEntry.objects.filter(admin_published=True)
    serializer_class = serializers.JournalEntrySerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class JournalEntryImageViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry model
    """

    queryset = models.JournalEntryImage.objects.filter(admin_published=True)
    serializer_class = serializers.JournalEntryImageSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class JournalEntryAnalysisCodeViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry Analysis Code model
    """

    queryset = models.JournalEntryAnalysisCode.objects.filter(admin_published=True)
    serializer_class = serializers.JournalEntryAnalysisCodeSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class JournalEntryAnalysisViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry Analysis model
    """

    queryset = models.JournalEntryAnalysis.objects.filter(admin_published=True)
    serializer_class = serializers.JournalEntryAnalysisSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
