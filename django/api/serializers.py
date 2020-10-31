from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = '__all__'


class JournalEntryTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JournalEntryTag
        fields = '__all__'


class JournalEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JournalEntry
        fields = '__all__'


class JournalEntryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JournalEntryImage
        fields = '__all__'
