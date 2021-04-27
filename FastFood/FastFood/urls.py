"""FastFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
<<<<<<< HEAD
from fastfoodapp.views import mainpage,typepage,restaurant_Reg,restaurant,addmeal,delete,afterReg,login,customer_reg,Rdessert,Rmeal,Outer_SearchBox,SearchBox,OrderPage
=======

from fastfoodapp.views import mainpage,typepage,restaurant_Reg,restaurant,addmeal,delete,customer,details,afterReg,login,customer_reg,Rdessert,Rmeal,Outer_SearchBox,SearchBox,Aboutus,User,curentuser
>>>>>>> 94df555cc48bb1c3d5d158509bcddcf00aa9a1dd


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainpage,name="MainPage"),
    path('typepage/',typepage,name="TypePage"),
    path('restaurantreg',restaurant_Reg,name="RegRestaurant"),
    path('restaurant',restaurant,name="Restaurant"),
<<<<<<< HEAD
    path('restaurant/<int:id>',delete,name="Restaurant"),
    path('restaurant/addmeal',addmeal,name="Addmeal"),  
=======
    path('customer',customer,name="Customer"),
    path('restaurant/<int:id>',delete,name="Delete"),
    path('restaurant/addmeal',addmeal,name="Addmeal"),  
    path('restaurant/details',details,name="Details"),  
>>>>>>> 94df555cc48bb1c3d5d158509bcddcf00aa9a1dd
    path('congratulations',afterReg,name="congratulations"),
    path('login/',login,name="login"),
    path('customer/',customer_reg ,name="customer"),
     path('RDFPage/',Rdessert ,name="RDFPage"),
     path('Rmeals/',Rmeal ,name="Rmeals"),
     path('Outer_SearchBox/',Outer_SearchBox ,name="search"),
     path('SearchBox/',SearchBox ,name="SearchBox"),
<<<<<<< HEAD
     path('OrderPage/',OrderPage ,name="OrderPage"),
=======
     path('about/',Aboutus,name="aboutus"),
     path('User/',User ,name="user"),
     path('User1/',curentuser,name="user1"),

>>>>>>> 94df555cc48bb1c3d5d158509bcddcf00aa9a1dd


]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
