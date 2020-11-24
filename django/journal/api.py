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
        permissions.IsAuthenticated,
    ]


class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry model
    """

    serializer_class = serializers.JournalEntrySerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def perform_create(self, serializer):
        """
        Add the 'user' field when creating a journal entry
        Get the user's ID from the request
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Only return journal entries for the currently authenticated user,
        and return them in descending order (newest first)
        """
        return models.JournalEntry.objects\
            .filter(admin_published=True, user=self.request.user)\
            .order_by('-meta_created_datetime')


class JournalEntryImageViewSet(viewsets.ModelViewSet):
    """
    Creates a ViewSet for managing CRUD operations on the Journal Entry model
    """

    queryset = models.JournalEntryImage.objects.filter(admin_published=True)
    serializer_class = serializers.JournalEntryImageSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]