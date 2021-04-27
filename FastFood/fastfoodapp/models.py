from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.



class Restaurant(models.Model):
    R_Name=models.CharField(max_length=200,unique=True)
    R_Type=models.CharField(max_length=200)
    R_Email=models.EmailField(max_length=200,unique=True)
    R_Phone=models.BigIntegerField(default=0,unique=True)
    R_Password=models.CharField(max_length=200)
    R_City=models.CharField(max_length=200)
    R_Area=models.CharField(max_length=200)
    R_Image = models.ImageField(upload_to='media/images', default="null")
    R_Rate= models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])



    class Meta:
        verbose_name_plural = 'Restaurants'
        
    def __str__(self):
        return self.R_Name





class FoodItem(models.Model):
    It_Name = models.CharField(max_length=200)
    It_Kind = models.CharField(max_length=200)
    It_Size = models.CharField(max_length=200)
    It_Prise = models.PositiveIntegerField(default= 0.0)
<<<<<<< HEAD
    It_Descrip = models.CharField(max_length=200, default='null')
=======
    It_Descrip = models.CharField(max_length=200,default="null")
>>>>>>> 94df555cc48bb1c3d5d158509bcddcf00aa9a1dd
    F_Images= models.ImageField(upload_to='media/images', default="null")
    F_Rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])




    def __str__(self):
        return self.It_Name
    



class Add(models.Model): 
    R_id = models.ForeignKey(Restaurant(), default=1 ,on_delete= models.SET_DEFAULT)
    F_id=models.ForeignKey(FoodItem(),default=1,on_delete=models.SET_DEFAULT)
    







class DeliveryInfo(models.Model):
    D_Name = models.CharField(max_length=200)
    D_time = models.DateTimeField()
    D_totalCost = models.FloatField()






class has(models.Model):
    Food_it_id = models.ForeignKey(FoodItem(),default=1 ,on_delete=models.SET_DEFAULT)
    Delivery_id= models.ForeignKey(DeliveryInfo(), default=1, on_delete=models.SET_DEFAULT)
    




class Customer(models.Model):
    C_Fname=models.CharField(max_length=200)
    C_Lname=models.CharField(max_length=200)
    C_Email=models.EmailField(max_length=200,unique=True)
    C_Password=models.CharField(max_length=200)
    C_Password2=models.CharField(max_length=200)
    C_Phone=models.CharField(max_length=200,unique=True)
    C_City=models.CharField(max_length=200)
    C_Area=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Customers'
        
    def __str__(self):
        return self.C_Fname




    




class Order(models.Model):
    Customer_id = models.ForeignKey(Customer(),default=1,on_delete=models.SET_DEFAULT)
    Food_it_id = models.ForeignKey(FoodItem(),default=1,on_delete=models.SET_DEFAULT)
    





class Receive(models.Model):
    Customer_id = models.ForeignKey(Customer(), default=1,on_delete=models.SET_DEFAULT)
    Delivery_id = models.ForeignKey(DeliveryInfo(), default=1, on_delete=models.SET_DEFAULT)
    



