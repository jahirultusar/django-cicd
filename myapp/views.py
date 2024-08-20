from django.shortcuts import render
from django.http import HttpResponse
import subprocess



# def index(request):
#     return render(request, 'myapp/index.html')

def index(request):
    git_hash, git_message = get_git_info()
    context = {
        'git_version': git_hash,
        'git_message': git_message
    }
    return render(request, 'myapp/index.html', context)

def get_git_info():
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()[:6]
        commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('ascii').strip()
        return commit_hash, commit_message
    except subprocess.CalledProcessError:
        return "unknown", "No commit message available"