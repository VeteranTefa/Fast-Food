from django.db import models

# Create your models here.



class Restaurant(models.Model):
    R_Name=models.CharField(max_length=200)
    R_Type=models.CharField(max_length=200)
    R_Email=models.EmailField()
    R_Phone=models.BigIntegerField(default=0)
    R_Password=models.CharField(max_length=200)
    R_City=models.CharField(max_length=200)
    R_Area=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Restaurants'
        
    def __str__(self):
        return self.R_Name

# # class Restaurant(models.Model):
# #     R_id = models.IntegerField(primary_key=True, serialize=True,default=1000)
# #     R_Fname = models.CharField(max_length=200)
# #     R_Lname = models.CharField(max_length=200)
# #     R_Rating= models.IntegerField(default=1)
# #     R_City  = models.CharField(max_length=200)
# #     R_Area  = models.CharField(max_length=200)



# #     class Meta:
# #         verbose_name_plural = 'Restaurants'



# #     def __str__(self):
# #         A = self.R_Fname +' ' + self.R_Lname
# #         return A





# # class RestContact(models.Model):
# #     Restaurant_id = models.ForeignKey(Restaurant , default=1 , on_delete=models.SET_DEFAULT)
# #     Restaurant_mobile = models.IntegerField()
# #     Restaurant_Telephone = models.IntegerField()
# #     Restaurant_Contact_pouplareName = models.CharField(max_length=200, default='The Contact Numbers')
    
    


# #     class Meta:
# #         verbose_name_plural = 'Restaurants Contacts'


# #     def __str__(self):
# #         return self.Restaurant_Contact_pouplareName



class FoodItem(models.Model):
    F_id = models.IntegerField(primary_key=True, default=101)
    It_Name = models.CharField(max_length=200)
    It_Kind = models.CharField(max_length=200)
    It_Size = models.CharField(max_length=200)




class Add(models.Model): 
    R_id = models.ForeignKey(Restaurant(), default=1 ,on_delete= models.SET_DEFAULT)
    F_id = models.ForeignKey(FoodItem(), default=1 ,on_delete= models.SET_DEFAULT)
    






class DeliveryInfo(models.Model):
    D_id = models.IntegerField(primary_key=True, default=201)
    D_Name = models.CharField(max_length=200)
    D_time = models.DateTimeField()
    D_totalCost = models.FloatField()



class has(models.Model):
    Food_it_id = models.ForeignKey(FoodItem(),default=101 ,on_delete=models.SET_DEFAULT)
    Delivery_id= models.ForeignKey(DeliveryInfo(), default=201, on_delete=models.SET_DEFAULT)
    


class Customer(models.Model):
    C_Fname=models.CharField(max_length=200)
    C_Lname=models.CharField(max_length=200)
    C_Email=models.EmailField()
    C_Password=models.CharField(max_length=200)
    C_Password2=models.CharField(max_length=200)
    C_Phone=models.CharField(max_length=200)
    C_City=models.CharField(max_length=200)
    C_Area=models.CharField(max_length=200)
# class Customer(models.Model):
#     C_id = models.IntegerField(primary_key=True, default=1000)
#     C_Fname = models.CharField(max_length=200)
#     C_Lname = models.CharField(max_length=200)
#     C_City  = models.CharField(max_length=200)
#     C_Area  = models.CharField(max_length=200)



# class CustContact(models.Model):
#     Customer_id = models.ForeignKey(Customer(), default=1000,on_delete=models.SET_DEFAULT)
#     Customer_mobile = models.IntegerField()
#     Customer_Telephone = models.IntegerField()
#     Customer_Email = models.EmailField()
    


class Order(models.Model):
    Customer_id = models.ForeignKey(Customer(),default=1,on_delete=models.SET_DEFAULT)
    Food_it_id = models.ForeignKey(FoodItem(),default=1,on_delete=models.SET_DEFAULT)
    



class Receive(models.Model):
    Customer_id = models.ForeignKey(Customer(), default=1,on_delete=models.SET_DEFAULT)
    Delivery_id= models.ForeignKey(DeliveryInfo(), default=1, on_delete=models.SET_DEFAULT)
    



