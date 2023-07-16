from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

def signupuser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user.save()
            login(request, user)
            return redirect('todocurrent')
    else: 
        form = SignUpForm()
        
    return render(request, 'todo/signupuser.html', {'form':form})

def todocurrent(request):
    return render(request, 'todo/todocurrent.html')