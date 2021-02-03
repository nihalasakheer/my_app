from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def index(request):
    return render(request, 'index.html')  

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('signup')
            else:        
               users = User.objects.create_user(username=username, password=password1, email=email)
               users.save()
               print('user created')
               return redirect('index')
        else:
            print('password is not matching....')
            return redirect('signup')
        return redirect('/')
    else:    
    
      return render(request, 'signup.html')      