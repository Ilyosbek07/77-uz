from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('UploadImage/', views.UploadImageView.as_view(), name='image_upload'),
    path('UploadFile/', views.UploadFileView.as_view(), name='file_upload'),
]
