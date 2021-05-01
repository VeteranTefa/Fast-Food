from django.contrib import admin
from .models import Restaurant
# from .models import RestContact
from .models import FoodItem
from .models import Add
from .models import DeliveryInfo
from .models import has
from .models import Customer
# from .models import CustContact
from .models import Order
from .models import Receive
# from .models import shop,meal,khod






# Register your models here.

admin.site.register(Restaurant)
# admin.site.register(RestContact)
admin.site.register(FoodItem)
admin.site.register(Add)
admin.site.register(DeliveryInfo)
admin.site.register(has)
admin.site.register(Customer)
# admin.site.register(CustContact)
admin.site.register(Order)
admin.site.register(Receive)
# admin.site.register(meal)
# admin.site.register(shop)
# admin.site.register(khod)




