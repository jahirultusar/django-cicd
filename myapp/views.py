from django.shortcuts import render
from django.http import HttpResponse
import subprocess



# def index(request):
#     return render(request, 'myapp/index.html')
def index(request):
    try:
        git_version, git_hash, git_message, git_date = get_git_info()
    except Exception as e:
        git_version, git_hash, git_message, git_date = ("Error fetching version", "unknown", "Error fetching message", "unknown")

    context = {
        'git_version': git_version,
        'git_hash': git_hash,
        'git_message': git_message,
        'git_date': git_date
    }
    return render(request, 'myapp/index.html', context)


# def get_git_info():
#     try:
#         commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()[:6]
#         commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('ascii').strip()
#         return commit_hash, commit_message
#     except subprocess.CalledProcessError:
#         return "unknown", "No commit message available"
    


# def get_git_info():
#     try:
#         commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()[:6]
#         # Fetching commit message and date with corrected command format
#         log_output = subprocess.check_output(['git', 'log', '-1', '--pretty=%B%n%ad', '--date=local']).decode('ascii').strip()
#         commit_message, commit_date = log_output.split('\n', 1)  # Splits the output into message and date
#         return commit_hash, commit_message, commit_date
#     except subprocess.CalledProcessError:
#         return "unknown", "No commit message available", "Date unknown"



#current

def get_git_info():
    try:
        # Fetch the latest Git tag
        latest_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode('ascii').strip()

        # Fetch the commit hash
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()[:6]

        # Fetch the commit message and date
        log_output = subprocess.check_output(['git', 'log', '-1', '--pretty=%B%n%ad', '--date=local']).decode('ascii').strip()
        commit_message, commit_date = log_output.split('\n', 1)  # Splits the output into message and date
        
        return latest_tag, commit_hash, commit_message, commit_date
    except subprocess.CalledProcessError:
        return "unknown", "unknown", "No commit message available", "Date unknown"
