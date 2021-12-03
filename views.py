from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


global myuser
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        address=request.POST['address']
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.email=email
        myuser.save()
        messages.success(request,"Your account has been successfully created.")
        return redirect('signin')
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            username=user.username
            email=user.email
            return render(request,"authentication/index.html",{'name':username,'email':email})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect('home')

def edit(request):
   

    return render(request,"authentication/edit.html")


def delete(request):
    myuser=User.objects.all()
    myuser.delete()
    return redirect('home')
        

