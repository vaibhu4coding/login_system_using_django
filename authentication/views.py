from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(username=username, password = pwd)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname':fname})
        else:
            messages.error(request, "Add Credentials")
            return redirect("http://localhost:8000/authentication/home/")
    return render(request, "authentication/signIn.html")

def signUp(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email_address']
        pass1 = request.POST['pwd']
        pass2 = request.POST['cnf_pwd']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('http://localhost:8000/authentication/home/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('http://localhost:8000/authentication/home/')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('http://localhost:8000/authentication/home/')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('http://localhost:8000/authentication/home/')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('http://localhost:8000/authentication/home/')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
        
        
        return redirect('http://localhost:8000/authentication/signin')
        
        
    return render(request, "authentication/signup.html")

def signOut(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('http://localhost:8000/authentication/home/')
