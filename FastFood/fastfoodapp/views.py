from django.shortcuts import render,HttpResponse
from django.urls import path
from . import models
from .models import Restaurant,FoodItem
from django.views.decorators.csrf import csrf_exempt





# Create your views here.

        # -----  Mubarak work Area  -----#
    # Main page function
def mainpage(request):
    Restobject = Restaurant.objects.all()
    return render(request,'mainPage.html',{'Restobject': Restobject})

    # Food Page function 
def Rdessert(request):
    dessert = FoodItem.objects.filter(It_Kind='Dessert')
    # print("hi")
    # for d in dessert:
    #     print("hello")
    #     print(d)
    return render(request,'html files/RDFPage.html',{'dessert' : dessert})



    # Search Fuchtion 
# def SearchBox(request):
#     print("hi")
#     if request.method == "GET":
#         searched = request.GET.get('searched')
#         FList = FoodItem.objects.all().filter(It_Name=searched)
#         print(FList)
#         return render(request, 'html files/test.html', {'searched':searched, 'FList' : FList})
#     else:
#         return render(request, 'html files/test.html', {})

@csrf_exempt
def Outer_SearchBox(request):
    if request.method == "POST":
        outer_search = request.POST.get('searched')
        Flist_two= FoodItem.objects.all().filter(It_Name=outer_search)
        print(Flist_two)
        return render(request, 'html files/test.html', {'outer_search': outer_search, 'Flist_two':Flist_two})
    else:
        return render(request, 'html files/test.html', {})




def Rmeal(request):
    meals = FoodItem.objects.all().filter(It_Kind='Meals')
    print(meals)
    return render(request, 'html files/RMFPage.html', {'meals':meals})



# def Hdessert(request):
#     return render(request,'html files/Hdessert.html',{})


# def Hmeal(request):
#     return render(request, 'html files/HMpage.html')


                # mubarak workespace end here 
        # --------------------------------------------------#





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

def login (request):
    return render(request,'login.html')

def customer_reg (request):
    return render(request,'registercustomer.html')




