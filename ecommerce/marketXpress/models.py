from django.db import models
# Product,Order,Customer,Category,Brand

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True,verbose_name='Category Name')
    description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, null=True,verbose_name='Brand Name')
    brand_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    # image = models.ImageField(upload_to='brands/', null=True)
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200, null=True,verbose_name='Product Name')
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True,verbose_name='Product Price')
    # 9999.99 4 2bl w 2 b3d kolo mayzedsh 3n 6 
    # price = models.FloatField()
    instock = models.BooleanField(default=True,null=True, blank=True)
    description = models.CharField(max_length=200, null=True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    product_category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE) #one to many relationship
    product_brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE) #one to many relationship

    
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
    name = models.CharField(max_length=200, null=True,verbose_name='Customer Name')
    # fname = models.CharField(max_length=200, null=True)
    # lname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    age= models.PositiveIntegerField(default=18)
    email = models.CharField(max_length=200, null=True)
    shippingAddress = models.CharField(max_length=255, null=True)
    customer_product = models.ManyToManyField(Product) #many to many relationship

    def is_adult(self):
        if self.age > 20:
            return True
        else:
            return False
    is_adult.short_description = 'Adult'
    is_adult.boolean = True



    def __str__(self):
        return self.name
        # return self.fname+''+self.lname

class Order(models.Model):          
    customer = models.ForeignKey('Customer', null=True, on_delete=models.CASCADE) #one to many relationship
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    # transaction_id = models.CharField(max_length=200, null=True)
    order_product = models.ManyToManyField(Product) #many to many relationship
    customer_order_date = models.DateTimeField(auto_now_add=True, null=True) 
    # quantity = models.PositiveIntegerField()

    def total_cost(self):
        total = 0
        order_items = self.orderitem_set.all()
        for item in order_items:
            total += item.product.price * item.quantity
        return total


    def total_cost(self):
        return self.price * self.quantity

    def free_Shipping():
        if self.total_cost() > 500:
            return True
        else:
            return False

    free_Shipping.short_description = 'FREE Shipping'        


    def formatted_order_date(self):
        return self.customer_order_date.strftime('%Y-%m-%d  @%H')


    def __str__(self):
        # return f"Order's ID {self.id} by {self.customer.name} on {self.customer_order_date}"     #date format till the seconds %H:%M:%S'
        return f"Order's ID {self.id} by {self.customer.name} on {self.formatted_order_date()}" #date format till the day

    # Total price
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems]) #list comprehension
        return total
    
    # Total Items
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems]) #list comprehension
        return total 

