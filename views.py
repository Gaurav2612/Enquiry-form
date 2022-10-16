from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    return render(request,'index.html')

def login(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            return HttpResponseRedirect('/enquiry')
        else:
            messages.error(request, "Invalid UserName or Password")
    return render(request,"login.html")
    
def signup(request):
    if(request.method == "POST"):
        type = request.POST.get("actype")
        if(type == "seller"):
            s = Seller()
            s.name = request.POST.get("name")
            s.username = request.POST.get("username")
            s.email = request.POST.get("email")
            s.phone = request.POST.get("phone")
            password = request.POST.get("password")
            cpassword = request.POST.get("cpassword")
            if(password == cpassword):
                try:
                    user = User.objects.create_user(
                        username=s.username, password=password, email=s.email)
                    user.save()
                    s.save()
                    return HttpResponseRedirect("/login")
                except:
                    messages.error(request, "User Name already Taken")

            else:
                messages.error(
                    request, "Password and Confirm Password Does not Match")
        else:
            pass
    return render(request, "signup.html")
 
def enquiry(request):
    user = User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin')
    else:
        seller = Seller.objects.get(username = request.user)
        return render(request,'sellerProfile.html',{"User":seller})
    return render(request,'enquiry.html')
