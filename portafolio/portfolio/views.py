from django.shortcuts import render
from .models import Project

def portfolio(request):
    projects = Project.objects.all()  
    return render(request, "portfolio/portfolio.html", {'projects':projects})

def detail(request, project_id=1):
    project = Project.objects.get(id=project_id)
    return render(request, "portfolio/project.html", {'project':project})
