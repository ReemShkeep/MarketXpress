from django.db import models
# Product,Order,Customer,Category

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    product_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL) #one to many relationship
    # product_category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE) #one to many relationship
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    # fname = models.CharField(max_length=200, null=True)
    # lname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    ShippingAddress = models.CharField(max_length=200, null=True)
    customer_order_date = models.DateTimeField(auto_now_add=True, null=True)
    customer_product = models.ManyToManyField(Product) #many to many relationship

    def __str__(self):
        return self.name
        # return self.fname+''+self.lname

class Order(models.Model):          
    customer = models.ForeignKey('Customer', null=True, on_delete=models.SET_NULL) #one to many relationship
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems]) #list comprehension
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems]) #list comprehension
        return total 

