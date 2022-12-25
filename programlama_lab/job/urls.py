from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job"),
    path("", views.job_list2, name="index"),
    path("<slug:category_slug>/<int:job_id>", views.job_detail, name="job-detail"),

    #path(route, view, opt(kısayol ismi))
    
]