from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def Login(request):
   if request.method=="POST":
       username=request.POST["username"]
       password=request.POST["password"]
       user=auth.authenticate(username=username,password=password)


       if user is not None:
           auth.login(request,user)
           return redirect("/")
       else:
           messages.info("invalid credentials")

           return redirect("log")


   return render(request,"login.html")
def Register(request):
    if request.method=='POST':
        username=request.POST["username"]
        firstname=request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                   messages.info(request,"already exists")
                   return redirect("reg")
            if User.objects.filter(email=email).exists():
                   messages.info(request," email already exists")
                   return redirect("reg")
            else:

                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect("log")



        else:
            messages.info(request ,"password not matching")
            return redirect("reg")
        return redirect("/")

    return render(request,"register.html")

def Logout(request):
    auth.logout(request)
    return redirect("/")
