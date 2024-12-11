from django.shortcuts import render,redirect
from .models import *
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, paginateProjects



def projects(request):
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects':projects, 'search_query':search_query, 'custom_range':custom_range}
    return render(request, "projects/projects.html", context)



def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    reviews = project.review_set.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.getVoteCount
        messages.success(request, 'Your review was successfully Created!')
        return redirect('single-project', pk=project.id)
    context = {'projects':project, 'reviews':reviews, 'form':form}
    return render(request, "projects/single-project.html", context)



@login_required(login_url='login')
def createProject(request):
    #profile is equal to logged-in user
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile   #-->project owner(one-to-many) is equal to logged-in user 
            project.save()
            messages.success(request, 'Project was Created successfully!')
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)



@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            messages.success(request, 'Project was Updated successfully!')
            return redirect('account')
            
    context = {'form':form, 'project':project}
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

