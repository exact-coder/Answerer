from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'authorization/pages/index.html')

def auth_login(request):
    return render(request, 'authorization/pages/auth_login.html')

def auth_register(request):
    return render(request, 'authorization/pages/auth_register.html')