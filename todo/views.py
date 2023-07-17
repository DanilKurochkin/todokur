from django.shortcuts import render, redirect
from .forms import SignUpForm, CreateTodoForm
from .models import Todo
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
    return render(request, 'todo/todocurrent.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
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

def create(request):
    if request.method == 'POST':
        form = CreateTodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('todocurrent')
    else:
        form = CreateTodoForm()
    return render(request, 'todo/todocreate.html', {'form':form })