from django.shortcuts import render
from django.http import HttpResponse


def project(request):
    return render(request, "projects/project.html")

def projects(request, pk):
    return HttpResponse("here" + ' ' + str(pk))