from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects,paginationProjects
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
# Create your views here.

def projects(request):

    projects=Project.objects.all()
    # projects,search_query = searchProjects(request)
    #
    # custom_range,projects = paginationProjects(request,projects,3)
    context = {
        'projects':projects,
        # 'query':search_query,
        # 'custom_range':custom_range,
    }
    print(request.user.profile.id==projects[0].owner.id)
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)

    context = {
        'project':projectObj,
    }
    return render(request,'projects/single_project.html',context)

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES) #ovo moramo da stavimo zbog slike
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect('/projects') #mogli smo i u form action da stavimo ovo
    context={'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk) #ovo radimo da ne bi neko ko zna rutu nekog posta, a ko nije vlasnik posta isti editovao
    form = ProjectForm(instance=project)
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES,instance=project) #da stalno ne bi pravio nove projecte
        if form.is_valid():
            project = form.save()
            return redirect('/projects') #mogli smo i u form action da stavimo ovo
    context={'form':form,'project':project}
    return render(request,'projects/project_form.html',context)



@login_required(login_url='login')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    project.delete()
    return redirect('/projects')


