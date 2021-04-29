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
from fastfoodapp.views import mainpage,typepage,restaurant_Reg,restaurant,addmeal,editmeal,delete,afterReg,login,customer_reg,Rdessert,  curentuser,User,Rmeal,Outer_SearchBox,SearchBox,OrderPage,Aboutus,loginRestuarnt,loginType,newUser,index




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainpage,name="MainPage"),
    path('typepage/',typepage,name="TypePage"),
    path('restaurantreg',restaurant_Reg,name="RegRestaurant"),
    path('restaurant',restaurant,name="Restaurant"),
    path('restaurant/<int:id>',delete,name="Restaurant"),
    path('restaurant/addmeal',addmeal,name="Addmeal"),
    path('restaurant/editmeal/<int:id>',editmeal,name="Editmeal"),  
    path('congratulations',afterReg,name="congratulations"),
    path('login/',login,name="login"),
    path('about/',Aboutus,name="aboutus"),
    path('customer/',customer_reg ,name="customer"),
    path('User/',User ,name="user"),
    path('User1/',curentuser,name="user1"),
    path('RDFPage/',Rdessert ,name="RDFPage"),
    path('Rmeals/',Rmeal ,name="Rmeals"),
    path('Outer_SearchBox/',Outer_SearchBox ,name="search"),
    path('SearchBox/',SearchBox ,name="SearchBox"),
    path('OrderPage/<int:id>',OrderPage ,name="OrderPage"),
    path('loginforrestuarnt/',loginRestuarnt ,name="login2"),
    path('loginType/',loginType ,name="loginType"),
    path('newuser/',newUser ,name="newuser"),
    path('index/<int:id>',index,name="index"),
    # path('home',OrderPage,name="home"),



]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
