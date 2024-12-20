from django.urls import path, include
from .views.file_views import FileUploadView
from django.contrib import admin 
from .views.users import GetAllUsers 

urlpatterns = [
    
    path('upload-file/', FileUploadView.as_view(), name='uploadfile'), 
    path('users/', GetAllUsers.as_view(), name='users') 
    
]
