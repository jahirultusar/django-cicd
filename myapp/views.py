from django.shortcuts import render
from django.http import HttpResponse
import subprocess



def index(request):
    return render(request, 'myapp/index.html')




def version_view(request):
    try:
        # Capture the latest commit hash
        commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode('utf-8')

        # Capture the latest commit message
        commit_message = subprocess.check_output(["git", "log", "-1", "--pretty=%B"]).strip().decode('utf-8')

        # Combine them into a version string
        version_info = f"Commit Hash: {commit_hash}\nCommit Message: {commit_message}"
    except subprocess.CalledProcessError:
        version_info = "Version information not available."

    return HttpResponse(version_info, content_type="text/plain")
