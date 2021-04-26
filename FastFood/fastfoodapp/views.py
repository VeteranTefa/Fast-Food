from django.shortcuts import render,HttpResponse
from . import models
import re
from django.contrib import messages
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
#function for aboutpage
def Aboutus(request):
    return render (request,'aboutpage.html')       

    
#function for loginpage
def login (request):
    return render(request,'login.html')
#function for register for customer page
def customer_reg (request):
    return render(request,'registercustomer.html')
#function for connect register for customer page with database
def User(request):
         C_Fname=request.POST['fname']
         C_Lname=request.POST['lname']
         C_Email=request.POST['email']
         C_Password =request.POST['password']
         C_Password2=request.POST['Rpassword']
         C_Phone=request.POST['phone']
         C_City=request.POST['city']
         C_Area =request.POST['area']
         #regphone=re.match("r01(0|1|2|5)[0-9]{8}", C_Phone)
         regname=re.match("^[a-zA-Z]*$",C_Fname)
         if not regname:
             messages.error(request,"name must be vaild")
             return render (request,'registercustomer.html')
         elif C_Password != C_Password2 :
             messages.error(request,"passwod must be equal Retypepassword")
             return render (request,'registercustomer.html')
         #elif not regphone:
              #messages.error(request,"phone must be egypt")
              #return render (request,'registercustomer.html')
        
         else:
             NewUser=models.Customer(C_Fname=C_Fname,C_Lname=C_Lname,C_Email=C_Email,
              C_Password=C_Password,C_Password2=C_Password2,C_Phone=C_Phone,C_City=C_City,C_Area=C_Area)
             NewUser.save()
             messages.info(request,"Successfully Registered")
             return render(request,'typePage.html')


#function for connect login page with database
def curentuser(request):
    if request.method=="POST":
        try:
            Userdetails=models.Customer.objects.get(C_Email=request.POST['email'],C_Password=request.POST['password'])
            request.session['email']=Userdetails.C_Email
            return render(request,'mainpage.html')
        except models.Customer.DoesNotExist as e:
            messages.success(request,'username/password invaild.........') 
    return render(request,'login.html')    