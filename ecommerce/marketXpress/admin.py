from django.contrib import admin
# from .models import Product, Customer, Order, Category
from .models import *
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)

# Register your models here.
