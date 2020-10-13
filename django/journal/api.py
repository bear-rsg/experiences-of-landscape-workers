from . import models, serializers
from rest_framework import viewsets, permissions


class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry model
    """

    queryset = models.JournalEntry.objects.all()
    serializer_class = serializers.JournalEntrySerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class JournalEntryImageViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry model
    """

    queryset = models.JournalEntryImage.objects.all()
    serializer_class = serializers.JournalEntryImageSerializer
    permission_classes = [
        permissions.AllowAny,
    ]