from django.shortcuts import render
from django.http import HttpResponse
from marketXpress.models import * 
from django.views.generic import *
from rest_framework import viewsets, Response
from marketXpress.serializers import *
# from marketXpress.models import Customer, Product, Order, Category, Brand
# from django.views.generic import View,ListView, DetailView
# from rest_framework.models import APIView




# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Home index.")


def getCustomer(request,u_id):
    customer=Customer.objects.get(id=u_id)
    return HttpResponse("You're looking at the user's page of ID  %s." % u_id)


def getAllCustomers(request):
    customers = Customer.objects.all()
    # context={'customers':customers}
    # if i need to count the number of customers
    context={'customers':customers,'count':customers.count()}
    return render(request, 'marketXpress/customer_detail.html', context)
    # return HttpResponse("You're from django.views.generic import View,ListView, DetailView
  

class customerListView(ListView):
    def get(self, request):
        customers = Customer.objects.all()
        context={'customers':customers,'count':customers.count()}       
        return render(request, 'marketXpress/customer_detail.html', context)


#generic view CBV class based view Types are:
# ListView, DetailView, CreateView, UpdateView, DeleteView
class getAllCustomersView(ListView):
    model = Customer
    template_name = 'marketXpress/customer_detail.html'

class getAllProductsView(ListView):
    model = Product
    template_name = 'marketXpress/product_detail.html'

# list all customers using generic view
