from django.shortcuts import render, reverse
from .models import User, UserProfile
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect


def dashboard(request):
    context = {

        'users': User.objects.all()

    }

    return render(request, 'users/dashboard.html',context)

def login(request):
    contex={}
    if request.method == 'POST':
        #sername= request.POST['user']
        #password = request.POST['password']
        user = authenticate(request, username= request.POST['username'], password = request.POST['password'] )
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('users:dashboard'))
        else:
            contex={'error':'Bad username or password'}
    return render(request,'users/login.html',contex)


def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def register(request):
   context = {}
   if request.method == "POST":
      password = request.POST['password']
      confirm_password = request.POST['confirm_password']
      user_name = request.POST['username']
      email = request.POST['email']
      if password == confirm_password:
            if User.objects.create_user(user_name, email, password):
               return HttpResponseRedirect(reverse('users:login'))
            else:
               context = {
                  'error': 'Could not create user account - please try again.'
               }
      else:
            context = {
               'error': 'Passwords did not match. Please try again.'
            }
   return render(request, 'users/create_user.html', context)
