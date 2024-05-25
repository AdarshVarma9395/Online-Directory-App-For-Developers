from django.shortcuts import render

def projects(request):
    context = {}
    return render(request, "projects/projects.html", context)

def singleProject(request, pk):
    context = {}
    return render(request, "projects/single-project.html", context)