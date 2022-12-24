from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="jobs"),
    path("<slug:category_slug>/<int:job_id>", views.job_detail, name="job-detail"),
    #path(route, view, opt(kısayol ismi))
    
]