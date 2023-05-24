from django.shortcuts import render
from django.http import HttpResponse
from marketXpress.models import * # Customer, Product, Order, Category, Brand
from django.views.generic import *   # ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets #permissions, generics, status, mixins, views,viewset, generics, filters, pagination, serializers,
from rest_framework.response import Response
from marketXpress.serializers import * # CustomerSerializer, ProductSerializer, OrderSerializer, CategorySerializer, BrandSerializer
# from rest_framework.models import APIView

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the Home index.")


# def getCustomer(request,u_id):
#     customer=Customer.objects.get(id=u_id)
#     return HttpResponse("You're looking at the user's page of ID  %s." % u_id)


# def getAllCustomers(request):
#     customers = Customer.objects.all()
#     # context={'customers':customers}
#     # if i need to count the number of customers
#     context={'customers':customers,'count':customers.count()}
#     return render(request, 'marketXpress/customer_detail.html', context)
#     # return HttpResponse("You're from django.views.generic import View,ListView, DetailView
  

# class customerListView(ListView):
#     def get(self, request):
#         customers = Customer.objects.all()
#         context={'customers':customers,'count':customers.count()}       
#         return render(request, 'marketXpress/customer_detail.html', context)


# #generic view CBV class based view Types are:
# # ListView, DetailView, CreateView, UpdateView, DeleteView
# class getAllCustomersView(ListView):
#     model = Customer
#     template_name = 'marketXpress/customer_detail.html'
# # list all customers using generic view


# def BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#     # permission_classes = [permissions.IsAuthenticated]


def BrandViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Brand.objects.all()
        brand = get_object_or_404(queryset, pk=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )        