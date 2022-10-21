from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('upload/image/', views.ImageUploadView.as_view(), name='image_upload'),
    path('upload/file/', views.FileUploadView.as_view(), name='file_upload'),
]
