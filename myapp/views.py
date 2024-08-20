from django.shortcuts import render
from django.http import HttpResponse
import os


def index(request):
    return render(request, 'myapp/index.html')



def version_view(request):
    version_file_path = os.path.join(os.path.dirname(__file__), '../version.txt')
    try:
        with open(version_file_path, 'r') as f:
            version_info = f.read()
    except FileNotFoundError:
        version_info = "Version information not available."
    return HttpResponse(version_info, content_type="text/plain")
