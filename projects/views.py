from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from users.models import Profile
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, "projects/single_project.html", context)


@login_required(login_url="users:login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(
            request.POST or None,
            files=request.FILES or None,
        )
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("projects:projects")
    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="users:login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(
        request.POST or None,
        files=request.FILES or None,
        instance=project,
    )
    if request.method == "POST":
        form = ProjectForm(
            request.POST or None,
            files=request.FILES or None,
            instance=project,
        )
        if form.is_valid():
            form.save()
            return redirect("projects:projects")
    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="users:login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects:projects")
    context = {"object": project}
    return render(request, "delete_object.html", context)
