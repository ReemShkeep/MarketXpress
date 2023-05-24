from django.urls import path
from marketXpress.views import * #BrandViewSet
#  customerListView, getAllCustomersView
from marketXpress import views


urlpatterns = [
    # path('home/', views.index),
    # path('users/<u_id>', views.getCustomer),
    # path('func', views.getAllCustomers),
    # path('class', customerListView.as_view()),
    # path('generic', getAllCustomersView.as_view()),
    # path('products', getAllProductsView.as_view()),
    path('brand', BrandViewSet.as_view({'get': 'list'}))
   

]