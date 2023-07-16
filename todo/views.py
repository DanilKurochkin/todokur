from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.

def signupuser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else: 
        form = SignUpForm()
    return render(request, 'todo/signupuser.html', {'form':form})