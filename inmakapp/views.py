from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Person
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    per=Person.objects.all()

    return render(request,"index.html",
                  {"result":obj,"human":per})

# def about(request):
#     return render(request,"about.html")

# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     mul=x*y
#     sub=x-y
#     div=x/y
#
#     return render(request,"result.html",{"result":res,"result2":mul,"result3":sub,"result4":div})