from django.shortcuts import render

def job_list(request):
    return render(request, 'job-list.html')
# Create your views here.
