from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login,logout
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


@login_required(login_url='login')
def User_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def library(request):
    return render(request,'library.html')


@login_required(login_url='login')
def add_books(request):
    if request.method=="GET":
        book=Book_Entry_Form()
        return render(request, 'add_books.html', context={'book':book})
    else:
        book=Book_Entry_Form(request.POST)
        if book.is_valid():
            book.save()
            return redirect('library')
    return render(request, 'add_books.html', context={'book':book})    

def edit_books(request, id):
    book= Book.objects.get(id=id)
    if request.method=="GET":
        book_edit=Book_Entry_Form(instance=book)
        return render(request, 'edit_books.html', context={'book_form':book_edit})
    else:
        book_edit=Book_Entry_Form(request.POST, instance=book)
        if book_edit.is_valid():
            book_edit.save()
            return redirect('library')
    return render(request, 'edit_books.html', context={'book_form':book_edit})  

def delete_books(request, id ):
    book= Book.objects.get(id=id)
    book.delete()
    return redirect('library')
    
def list_books(request):
    list_book=Book.objects.all()
    return render(request, 'list_books.html', context={'list_book':list_book})
    