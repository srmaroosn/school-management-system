from email import message
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login,logout
from django.shortcuts import redirect, render
from .forms import *

# Create your views here.
def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        return render(request,'login.html',context={})
    


def register(request):
    if  request.method=="GET":
        form=studentregisterform()
        return render(request, 'register.html', context={'form':form})
    else:
        form=studentregisterform(request.POST)
        if form.is_valid:
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
    return render(request, 'register.html', context={'form':form})

def home(request):
    return render(request,'home.html')