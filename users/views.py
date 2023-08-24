from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from .form import RegisterUserForm
from .models import User

def register_purchaser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_purchaser = True
            var.save()
            messages.success(request,"Account Created Please Login to Continue")
            return redirect("login")
        else:
            messages.warning(request,"Something went wrong, please check the Inputs and try again")
            return redirect("register-purchaser")
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request,'users/register_purchaser.html',context)
    
def register_warehouse(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_warehouse = True
            var.save()
            messages.success(request,"Account Created Please Login to Continue")
            return redirect("login")
        else:
            messages.warning(request,"Something went wrong, please check the Inputs and try again")
            return redirect("register-purchaser")
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request,'users/register_purchaser.html',context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'You are logged in as {user}')
            return redirect('dashboard') 
        else:
            messages.warning(request, 'Something went wrong, please check the credentials and try again')
            return redirect('login') 
    else:
        return render(request, 'users/login.html')
        
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Session ended. Please log in to continue')
    return redirect('login')