from django.shortcuts import render,redirect
from .models import *
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, "projects/projects.html", context)

def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'projects':project}
    return render(request, "projects/single-project.html", context)

@login_required(login_url='login')
def createProject(request):
    #profile is equal to logged-in user
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile   #-->project owner(one-to-many) is equal to logged-in user 
            project.save()
            messages.success(request, 'Project was Created successfully!')
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project was Updated successfully!')
            return redirect('account')
            
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project was Deleted successfully!')
        return redirect('projects')
    context = {'object':project}
    return render(request, 'delete_template.html', context)

