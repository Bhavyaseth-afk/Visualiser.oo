from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from visualiser.settings import MEDIA_ROOT

class FileUploadView(APIView):
    def post(self, request, format=None):
        file_obj = request.FILES['file']
        file_name = file_obj.name
        print("Uploaded file name:", file_name)

        # Save the file to the media folder
        media_root = MEDIA_ROOT
        file_path = os.path.join(media_root, file_name)
        print("File path:", file_path)

        with open(file_path, 'wb+') as file:
            for chunk in file_obj.chunks():
                file.write(chunk)

        return Response({'message': 'File uploaded successfully'})

