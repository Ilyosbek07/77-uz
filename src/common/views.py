from django.shortcuts import render
from rest_framework import parsers, renderers, generics

from src.common import models, serializers


class ImageUploadView(generics.CreateAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageCreateSerializer


class FileUploadView(generics.CreateAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    queryset = models.File.objects.all()
    serializer_class = serializers.FileCreateSerializer
