from django.shortcuts import render


# Create your views here.

def mainpage(request):
    return render(request,'mainPage.html',{})

def typepage(request):
    return render(request,'typePage.html',{})

def restaurant_Reg(request):
    return render(request,'regestrationforrestuarnt.html',{})

def restaurant(request):
    return render(request,'restaurant.html')