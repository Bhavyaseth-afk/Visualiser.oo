
from django.urls import path, include
from visualapp import views

urlpatterns = [
    path('insert', views.FileUploadView.as_view(), name = 'file_uplaod'),  
]
