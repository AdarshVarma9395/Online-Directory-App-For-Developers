from django.shortcuts import render

def projects(request):
    context = {}
    return render(request, "projects.html", context)

def singleProject(request, pk):
    context = {}
    return render(request, "single-projects.html", context)