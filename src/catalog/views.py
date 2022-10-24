from django.shortcuts import render
from rest_framework import parsers, renderers, generics

from . import models, serializers


class UploadImageView(generics.CreateAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageCreateSerializer


class UploadFileView(generics.CreateAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    queryset = models.File.objects.all()
    serializer_class = serializers.FileCreateSerializer
