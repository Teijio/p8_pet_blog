from django.urls import path
from . import views

app_name = "pro"

urlpatterns = [
    path("project/",  views.project, name="project"),
    path("projects/",  views.projects, name="projects"),
]
