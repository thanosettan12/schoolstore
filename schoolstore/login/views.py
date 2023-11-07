from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm



def user_login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('login:profile')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login:login')


    else:
        return render(request, 'login.html')


def user_logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    return  render(request,'service.html')



def popup(request):
    return render(request, 'popup.html')




def submit_form(request):

    return render(request, 'form.html')