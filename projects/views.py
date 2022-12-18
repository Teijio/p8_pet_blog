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
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(
            request.POST or None,
            files=request.FILES or None,
        )
        if form.is_valid():
            form_save = form.save(commit=False)
            if form_save.owner:
                form_save.save()
            else:
                form_save.owner = Profile.objects.get(user=request.user)
                form_save.save()
            return redirect("projects:projects")
    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="users:login")
def update_project(request, pk):
    project = Project.objects.get(id=pk)
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
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects:projects")
    context = {"project": project}
    return render(request, "projects/delete_object.html", context)
