from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles,paginationProfiles
from .forms import CustomUserCreationForm,ProfileForm
from .models import Profile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
# from projects.models import Project

# Create your views here.
def profiles(request):


    profiles,search_query = searchProfiles(request)

    custom_range,profiles = paginationProfiles(request,profiles,3)


    context = {
        'profiles':profiles,
        'query':search_query,
        'custom_range':custom_range
    }
    return render(request,'users/profiles.html',context)

def profile(requset,pk):
    profile = Profile.objects.get(id=pk)
    projects = Project.objects.filter(owner=profile)
    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description__exact='')
    context = {
        'profile':profile,
        'projects':projects,
        'topSkills':topSkills,
        'otherSkills':otherSkills,
    }
    return render(requset,'users/user_profile.html',context)

@login_required(login_url='login') #ako nismo ulogovani redirectuj na login page
def userAccount(request):
    user = request.user #ovako uzimamo ulogovanog usera
    profile = user.profile #OneToOne relacija da bismo uzeli Profile koji odgovara user
    projects = profile.project_set.all()
    context={'profile':profile,'projects':projects}
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request,'users/profile_form.html',context)

# index, show, create, store, edit, update, destroy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!