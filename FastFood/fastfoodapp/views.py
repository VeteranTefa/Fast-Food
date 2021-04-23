from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.

def mainpage(request):
    return render(request,'mainPage.html',{})

def typepage(request):
    return render(request,'typePage.html',{})

def restaurant_Reg(request):
    return render(request,'regestrationforrestuarnt.html',{})

def restaurant(request):
    return render(request,'restaurant.html',{})

def afterReg(request):
    res_name=request.POST['restname']
    res_type=request.POST['restype']
    res_email=request.POST['email']
    res_password=request.POST['pass']
    res_phone=request.POST['phone']
    res_city=request.POST['city']
    res_area=request.POST['area']
    reg=models.Restaurant(R_Name=res_name,R_Type=res_type,R_Email=res_email,R_Password=res_password,
        R_Phone=res_phone,R_City=res_city,R_Area=res_area)
    
    reg.save()
    return HttpResponse("Your Data Saved ")