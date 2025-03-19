from django.shortcuts import render,redirect
from .forms import completeprofile
from django.contrib.auth.models import User
from .models import profile
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request,'landing.html')

@login_required
def dashboard(request):
    duser=profile.objects.get(username=request.user)
    return render(request,'dashboard.html',{'duser':duser})

@login_required
def profilef(request):
    try:
        profiled = profile.objects.get(username=request.user)
        if profiled.is_completed:  
            return redirect('dashboard') 
    except profile.DoesNotExist:
        profiled = None
    if request.method == 'POST':
        form = completeprofile(request.POST)
        if form.is_valid():
            profile_instance = form.save(commit=False)  
            profile_instance.username = request.user    
            profile_instance.iscompleted = True         
            profile_instance.save()                    
            return redirect('dashboard')  
    else:
        form = completeprofile()
    return render(request, 'users/profile.html', {'form': form})

def login(request):
    user = None
    error_message = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            authlogin(request, user)
            try:
                complete = profile.objects.get(username=user)
                return redirect('dashboard') if complete.iscompleted else redirect('profile')
            except profile.DoesNotExist:
                return redirect('profile')
        else:
            error_message = "Invalid credentials"
    return render(request, "users/login.html", {"user": user, "error_message": error_message})

@login_required
def logout(request):
    authlogout(request)
    return redirect('landing')

def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=username,email=email,password=password) 
        except Exception as e:  
            error_message=str(e)
    return render(request, "users/signup.html",{"user":user,"error_message":error_message})
