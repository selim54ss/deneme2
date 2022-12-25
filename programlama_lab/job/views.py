from django.shortcuts import render
from . models import Job

def job_list(request):

    job = Job.objects.all()

    context = {
        'job' : job

    }

    return render(request, 'job-list.html', context)
    
def job_list2(request):

    index = Job.objects.all()

    context = {
        'index' : index

    }

    return render(request, 'index.html', context)
# Create your views here.
def job_detail(request, category_slug, job_id):
    job_detail= Job.objects.get(category_id__slug=category_slug, id = job_id)
    
    context = {
        'job_detail' : job_detail

    }

    return render(request, 'job-detail.html', context)



