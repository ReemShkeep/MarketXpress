from rest_framework import serializers
from .models import *




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'created_at', 'updated_at']
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        #read_only_fields = ['id', 'created_at', 'updated_at']
        # fields = ['id', 'fname', 'lname', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'created_at', 'updated_at']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['id', 'customer', 'product', 'quantity', 'price', 'order_date', 'status', 'created_at', 'updated_at']



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['id', 'name', 'price', 'description', 'category', 'stock', 'image', 'created_at', 'updated_at']

