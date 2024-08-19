from django.shortcuts import render
import subprocess
from django.http import HttpResponse

def index(request):
    return render(request, 'myapp/index.html')


def version_view(request):
    try:
        # Get the latest Git tag
        version = subprocess.check_output(["git", "describe", "--tags"]).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        version = "No version found"
    return HttpResponse(version, content_type="text/plain")
