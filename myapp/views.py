from django.shortcuts import render
# from django.http import HttpResponse
import subprocess



# def index(request):
#     return render(request, 'myapp/index.html')

def index(request):
    git_hash, git_message, git_date = get_git_info()
    context = {
        'git_version': git_hash,
        'git_message': git_message,
        'git_date': git_date
    }
    return render(request, 'myapp/index.html', context)


# def get_git_info():
#     try:
#         commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()[:6]
#         log_output = subprocess.check_output(['git', 'log', '-1', '--pretty=%B%n%ad', '--date=local']).decode('ascii').strip()
#         commit_message, commit_date = log_output.split('\n', 1)  # Splits the output into message and date
#         latest_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode('ascii').strip()

#         return commit_hash, commit_message, commit_date, latest_tag

#     except subprocess.CalledProcessError:
#         # If there's an error, possibly because there are no tags yet, handle gracefully
#         return "unknown", "No commit message available", "Date unknown", "No tag available"



def get_git_info():
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()[:6]
        # Fetching commit message and date with corrected command format
        log_output = subprocess.check_output(['git', 'log', '-1', '--pretty=%B%n%ad', '--date=local']).decode('ascii').strip()
        commit_message, commit_date = log_output.split('\n', 1)  # Splits the output into message and date
        return commit_hash, commit_message, commit_date
    except subprocess.CalledProcessError:
        return "unknown", "No commit message available", "Date unknown"


# def get_git_info():
#     try:
#         commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()[:6]
#         log_output = subprocess.check_output(['git', 'log', '-1', '--pretty=%B%n%ad', '--date=local']).decode('ascii').strip()
#         commit_message, commit_date = log_output.split('\n', 1)
#         try:
#             # Attempt to fetch the latest tag
#             # latest_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode('ascii').strip()
#             detailed_tag = subprocess.check_output(['git', 'describe', '--tags', '--long']).decode('ascii').strip()
#         except subprocess.CalledProcessError:
#             # If no tags could be described, handle gracefully
#             # latest_tag = "No tag available"
#             detailed_tag = "no tag available"
#         return commit_hash, commit_message, commit_date, detailed_tag, #latest_tag
#     except subprocess.CalledProcessError:
#         return "unknown", "No commit message available", "Date unknown", "No tag available"
