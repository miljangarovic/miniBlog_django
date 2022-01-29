from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles,paginationProfiles
from .forms import CustomUserCreationForm,ProfileForm
from .models import Profile
from projects.models import Project
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
# from projects.models import Project
from django.contrib import messages

# Create your views here.
def profiles(request):


    profiles=Profile.objects.all()
    # profiles,search_query = searchProfiles(request)

    # custom_range,profiles = paginationProfiles(request,profiles,3)


    context = {
        'profiles':profiles,
        # 'query':search_query,
        # 'custom_range':custom_range
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



def loginUser(request):
    page='login'
    context = {'page':page}
    if request.user.is_authenticated: #ukoliko smo ulogovani da nebismo mogli opet da pristupimo login stranici
        return redirect('profiles')

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')


        user = authenticate(request,username=username,password=password) #ova funkcija provjerava da li se password odgovara username-u
        # ova funckija vraca user-a ako se podaci poklapaju, ili vraca Null ako se ne poklapaju
        if user is not None: #ako user postoji, tj. ako se podaci poklapaju
            login(request,user) # ova funkcija automatski formira session u bazi podataka, i takodje session se dodaje u browser cookies(da bi mogli da ostanemo ulogovani duze vrijeme)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'login_register.html',context)

def logoutUser(requset):
    logout(requset)
    messages.info(requset,'User was logged out!')
    return redirect('profiles')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #ovako pravimo user-a na osnovu podataka iz forme, ali ne zelimo jos da zavrsimo
            user.username = user.username.lower()
            user.save() #prije nego sto smo prihvatili sve podatke i upisali ih u bazu, sva slova smo podesili da budu mala

            messages.success(request,'User account was created!')
            login(request,user) #nakon sto ga registrujemo, user-a ulogujemo
            return redirect('/')
        else:
            messages.error(request,'An error has occurred during registration')

    context={'page':page,'form':form}
    return render(request,'login_register.html',context)

# index, show, create, store, edit, update, destroy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!