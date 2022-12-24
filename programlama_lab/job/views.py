from django.shortcuts import render
from . models import Job

def job_list(request):

    job = Job.objects.all()

    context = {
        'job' : job

    }

    return render(request, 'job-list.html', context)
    
# Create your views here.
