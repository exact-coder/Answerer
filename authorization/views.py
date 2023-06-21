from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request,'authorization/pages/dashboard.html')

def auth_login(request):
    return render(request, 'authorization/pages/auth_login.html')

def auth_register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'].replace(' ','').lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not password1 == password2:
            messages.error(request,"Passwords do not match")
            return redirect('auth_register')
        if User.objects.filter(username = username).exists():
            messages.error(request,f"{username} username already taken")
            return redirect('auth_register')
        if User.objects.filter(email = email).exists():
            messages.error(request,f"{email},email already exists")
            return redirect('auth_register')
        
        user = User.objects.create_user(email=email,username=username,password=password1)
        user.save()
        messages.success(request,f"{username}, created successfully")
        auth.login(request,user)
        return redirect('home')
    return render(request, 'authorization/pages/auth_register.html')