

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
# Create your views here.
from django.http import request
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import UserRegisterForm,LoginForm,UserEditForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission, User

def register(request):
    if request.user.is_authenticated:
        messages.success(request,"You already have logged-in in your current account.")
        return redirect('')
    elif request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            #Automate Logged in new Signup user
            login(request, new_user)
            #return redirect("accounts:signup_done")
            return redirect('core:home')
    else:
        user_form = UserRegisterForm()
    return render(request,'accounts/register.html',{'user_form': user_form})






def user_login(request):
    if request.user.is_authenticated:
        msg = messages.success(request,"You Already have account.")
        return redirect('')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('core:home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("accounts:login")



@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User Details updated '\
                                    'successfully')
            #return redirect('accounts:dashboard')
            return redirect('core:home')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,
                'accounts/edit.html',
                {'user_form': user_form,})






@login_required
def dashboard(request):
    return render(request,
                'accounts/dashboard.html')




