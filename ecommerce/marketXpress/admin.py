from django.contrib import admin
# from .models import Product, Customer, Order, Category
from .models import *
# tuble (), liist [], dictiomary {}
class CustomCustomer(admin.ModelAdmin):
  fieldsets = (
    ["Customer's Information",{'fields':['name','phone','age','email','shippingAddress']}],
    ["Order's Information",{'fields':['customer_product'] }]
  )
  list_display = ['name','phone','age','email','shippingAddress','is_adult']

#   fieldsets = (
#     ["Customer's Information",{'fields':['name','phone','email','shippingAddress']}],
#     ["Order's Information",{'fields':['customer_order_date ','customer_product'] }]
#   )
class InlineProduct(admin.StackedInline):
    model = Product
    extra = 1

class CustomCategory(admin.ModelAdmin):
    inlines = [InlineProduct]
    list_display = ['name','description']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 15
    list_editable = ['description']
    fieldsets = (
        ["Category's Information", {'fields': ['name', 'description']}],
    )

class CustomOrder(admin.ModelAdmin):
    list_display = ['order_date', 'customer_name', 'total_price']
    search_fields = ['order_date', 'customer_name']
    list_filter = ['order_date', 'customer_name']
    list_per_page = 15
    fieldsets = (
        ["Order's Information", {'fields': ['order_date', 'customer_name', 'total_price','free_Shipping']}],
    )


admin.site.register(Customer,CustomCustomer)
admin.site.register(Category,CustomCategory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Brand)

# admin.site.register(Product)
# admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(Category)


# Register your models here.






