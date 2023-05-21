from django.contrib import admin
# from .models import Product, Customer, Order, Category
from .models import *
# tuble (), liist [], dictiomary {}
class CustomCustomer(admin.ModelAdmin):
  fieldsets = (
    ["Customer's Information",{'fields':['name','phone','email','shippingAddress']}],
    ["Order's Information",{'fields':['customer_order_date ','customer_product'] }]
  )


# admin.site.register(Product,)
admin.site.register(Customer,CustomCustomer)
# admin.site.register(Order)
# admin.site.register(Category)

# Register your models here.
