from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def redirecttohome(request):
    return redirect('home')

def signupuser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password'])
            user.save()
            login(request, user)
            return redirect('todocurrent')
    else: 
        form = SignUpForm()
        
    return render(request, 'todo/signupuser.html', {'form':form})

def todocurrent(request):
    return render(request, 'todo/home.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        form.is_valid()
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'todo/login.html', 
                          {'form':form,
                           'error':'Incorrect username or password'})
        login(request, user)
        return redirect('todocurrent')
    else: 
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form':form})