from django.shortcuts import render,HttpResponse,redirect
from . import models
import re
from django.contrib import messages
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant,FoodItem,testModel


# Create your views here.



        #       Mubarak Functions workplace        #

def mainpage(request):
    Restobject = Restaurant.objects.all()
    Foods = FoodItem.objects.all()
    
    return render(request,'Mubarak html files/mainPage.html',{'Restobject': Restobject[0:3], 'Foods': Foods[0:3]})




    # Food Page function 
def Rdessert(request):
    dessert = FoodItem.objects.filter(It_Kind='Dessert')
    # print("hi")
    # for d in dessert:
    #     print("hello")
    #     print(d)
    return render(request,'Mubarak html files/RDFPage.html',{'dessert' : dessert})



def Rmeal(request):
    meals = FoodItem.objects.all().filter(It_Kind='Meals')
    # print(meals)
    return render(request, 'Mubarak html files/RMFPage.html', {'meals':meals})



        # Search Fuchtion 
def SearchBox(request):
    print("hi")
    if request.method == "GET":
        searched = request.GET.get('searched')
        FList = FoodItem.objects.all().filter(It_Name=searched)
        print(FList)
        return render(request, 'Mubarak html files/test.html', {'searched':searched, 'FList' : FList})
    else:
        return render(request, 'Mubarak html files/test.html', {})


@csrf_exempt
def Outer_SearchBox(request):
    if request.method == "POST":
        outer_search = request.POST.get('searched')
        Flist_two= FoodItem.objects.all().filter(It_Name=outer_search)
        # print(Flist_two)
        return render(request, 'Mubarak html files/test.html', {'outer_search': outer_search, 'Flist_two':Flist_two})
    else:
        return render(request, 'Mubarak html files/test.html', {})


def index(request, id):
    # itemId = testModel.objects.all()
    tesItem= testModel.objects.get(Mid=id)
    print(tesItem)
    return render(request, 'Mubarak html files/base.html', {
        # 'item': item.It_Name,
        # 'itemId': itemId,
        'tesItem': tesItem.MName ,
          
    })


def OrderPage(request, id):
    order = FoodItem.objects.get(id=id)
    print(order)
    return render(request, 'Mubarak html files/OrdersPage.html', {
        'order': order,
        'orderName': order.It_Name,
        'orderKink': order.It_Kind,
        'orderSize': order.It_Prise,
        'orderDescription': order.It_Descrip,
        'orderImages': order.F_Images,
        'orderRate': order.F_Rate
    })


              # mubarak workespace end here 
        # --------------------------------------------------#



def typepage(request):
    return render(request,'typePage.html',{})

def restaurant_Reg(request):
    return render(request,'regestrationforrestuarnt.html',{})

def details(request):
    return render(request,'details.html',{})

def customer(request):
    return render(request,'customer.html',{})


def restaurant(request):
#DELETD FROM DATABASE
    
 #RETRIVE FROM DATABASE
    foods_details = FoodItem.objects.all()
#    foods_list=[]
 #   for meal in foods_details:
  #      foods_list.append(meal.It_Name)
   #     foods_list.append(meal.It_Size)
    #    foods_list.append(meal.It_Kind)
    
    #print(foods_list)

    return render(request,'restaurant.html',{'foods_details' : foods_details})

def addmeal(request):
    #ADD TO DATABASE
    if request.method == 'POST':
        item_name = request.POST['item_name']
        item_size = request.POST['item_size']
        item_kind = request.POST['item_kind']
        item_prise = request.POST['item_prise']
        item_descrip = request.POST['item_descrip']
        F_Images  = request.POST['item_Image']

        foods = FoodItem.objects.create(
            It_Name = item_name,
            It_Size = item_size,
            It_Kind = item_kind,
            It_Prise = item_prise,
            It_Descrip = item_descrip,
            F_Images= F_Images
        )
    return render(request,'addmeal.html',{})


def delete(request,id):
#DELETD FROM DATABASE
    if request.method == 'POST':
        obj = FoodItem.objects.get(id=id)
        obje.delete()
        return redirect('restaurant.html')


def afterReg(request):
    res_name=request.POST['restname']
    res_type=request.POST['restype']
    res_email=request.POST['email']
    res_password=request.POST['pass']
    res_phone=request.POST['phone']
    res_city=request.POST['city']
    res_area=request.POST['area']
       # error_message=None
    # if not res_name:
    #     error_message="Restuarant Name Is Required"
    # elif len(res_name)<2:
    #         error_message="Restuarant Name must be 2 char or more "

    # elif res_type:
    #     error_message="Restuarant Type Is Required"
    # elif not res_email:
    #     error_message=" Email Is Required"
    # elif not res_password:
    #     error_message="Password Is Required"
    # elif not res_phone:
    #     error_message="Phone Is Required"
    # elif not res_city:
    #     error_message="City Is Required"
    # elif not res_area:
    #     error_message="Area Is Required"
    regphone=re.match(r"01(0|1|2|5)[0-9]{8}",res_phone)
    regpass=re.match(r"^[a-z0-9]{6,20}$",res_password)
    if regphone and regpass:
        reg=models.Restaurant(R_Name=res_name,R_Type=res_type,R_Email=res_email,R_Password=res_password,
                R_Phone=res_phone,R_City=res_city,R_Area=res_area)
        reg.save()
        messages.info(request,"Successfully Registered")
        return render(request,"regestrationforrestuarnt.html")
        # return HttpResponse("Successfully")
    else:
        if not regphone:
            messages.info(request,"Phone Invalid Plz Enter an Egyptian Phone Number ex:010..|011..|012..|015..")
        elif not regpass:
            messages.info(request,"Password Must be a letters or numbers and at least 6 characters")

        return render(request,"regestrationforrestuarnt.html")
        


    
def Aboutus(request):
    return render (request,'aboutpage.html',{})     

def login(request):
    return render(request,'login.html')

def customer_reg (request):
    return render(request,'registercustomer.html')


def User(request):
         C_Fname=request.POST['fname']
         C_Lname=request.POST['lname']
         C_Email=request.POST['email']
         C_Password =request.POST['password']
         C_Password2=request.POST['Rpassword']
         C_Phone=request.POST['phone']
         C_City=request.POST['city']
         C_Area =request.POST['area']
         regphone=re.match(r"01(0|1|2|5)[0-9]{8}", C_Phone)
        #  regname=re.match("^[a-zA-Z]*$",C_Fname)
        #  if not regname:
        #      messages.error(request,"name must be vaild")
        #      return render (request,'registercustomer.html')
         if C_Password == C_Password2 and regphone:
            NewUser=models.Customer(C_Fname=C_Fname,C_Lname=C_Lname,C_Email=C_Email,
              C_Password=C_Password,C_Password2=C_Password2,C_Phone=C_Phone,C_City=C_City,C_Area=C_Area)
            NewUser.save()
            messages.info(request,"Successfully Registered")
            return render(request,'registercustomer.html')
         else:
            if C_Password != C_Password2:
                messages.error(request,"Password must be equal Retype Password")
                return render(request,'registercustomer.html')
            elif not regphone:
                messages.error(request,"phone must be egypt")
                return render (request,'registercustomer.html')



            #  messages.error(request,"passwod must be equal Retypepassword")
            #  return render (request,'registercustomer.html')
        #  elif not regphone:
        #       messages.error(request,"phone must be egypt")
        #       return render (request,'registercustomer.html')
        
         
            


#function for connect login page with database
def curentuser(request):
    if request.method=="POST":
        try:
            Userdetails=models.Customer.objects.get(C_Email=request.POST['email'],C_Password=request.POST['password'])
            request.session['email']=Userdetails.C_Email
            return render(request,'Mubarak html files/mainpage.html')
        except models.Customer.DoesNotExist as e:
            messages.success(request,'username/password invaild.........') 
    return render(request,'login.html')

def newUser(request):
    if request.method=="POST":    
        try:
            userrest=models.Restaurant.objects.get(R_Email=request.POST['email'],R_Password=request.POST['pass']) 
            request.session['email']=userrest.R_Email
            return render(request,'Mubarak html files/mainpage.html',{'userrest':userrest})
        except models.Restaurant.DoesNotExist as e:
            messages.success(request,'Email or Password Invalid') 
    return render(request,'loginForRestuarant.html')  

def loginRestuarnt(request):
    return render(request,'loginForRestuarant.html',{})

def loginType(request):
    return render(request,'loginType.html',{})