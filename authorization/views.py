from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages

# Create your views here.

def anonymous_required(function = None, redirect_url = 'home'):

    if not redirect_url:
        redirect_url =redirect_url
    
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url= redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

@login_required(login_url="auth_login")
def dashboard(request):
    return render(request,'authorization/pages/dashboard.html')

@login_required(login_url="auth_login")
def user_profile(request):
    return render(request,'authorization/pages/user_profile.html')

@login_required(login_url="auth_login")
def user_profile_edit(request):
    return render(request,'authorization/pages/user_profile_edit.html')

@anonymous_required
def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user :
            auth.login(request,user)
            return redirect('user_profile')
        messages.error(request,"You give Wrong Information or User does not Exist!!")
        return redirect('auth_login')

    return render(request, 'authorization/pages/auth_login.html')


@anonymous_required
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