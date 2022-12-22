from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="jobs"),
    
    #path(route, view, opt(kısayol ismi))
    
]