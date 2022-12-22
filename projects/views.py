from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .utils import search_projects, paginator_projects
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm


def projects(request):
    projects, search_query = search_projects(request)
    custom_range, projects = paginator_projects(request, projects, 3)
    context = {
        "projects": projects,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.get_vote_count
        # update later ^
        messages.success(request, "Your review was successfully submitted!")
        return redirect("projects:project", pk=project.id)
    context = {"project": project, "form": form}
    return render(request, "projects/single_project.html", context)


@login_required(login_url="users:login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        new_tags = (
            request.POST.get("new_tags").replace(",", " ").upper().split()
        )
        form = ProjectForm(
            request.POST or None,
            files=request.FILES or None,
        )
        if form.is_valid():
            project = form.save()
            project.owner = profile
            project.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

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
        new_tags = (
            request.POST.get("new_tags").replace(",", " ").upper().split()
        )
        form = ProjectForm(
            request.POST or None,
            files=request.FILES or None,
            instance=project,
        )
        if form.is_valid():
            project = form.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
                
            return redirect("projects:projects")
    context = {"form": form, "project": project}
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
