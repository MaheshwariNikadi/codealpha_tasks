from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def home(request):
    return render(request, 'home.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def create_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        project = form.save(commit=False)
        project.created_by = request.user
        project.save()
        return redirect('project_list')

    return render(request, 'create_project.html', {'form': form})