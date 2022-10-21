from rest_framework import serializers

from src.common import models


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ('content', 'id')


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ('content', 'id')
