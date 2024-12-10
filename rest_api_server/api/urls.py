from django.urls import path
from .views.file_views import FileUploadView

urlpatterns = [
path('upload-file/', FileUploadView.as_view(), name='upload-file')
]
