from django.urls import path, include
from rest_framework import serializers
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name= "products_list"),
    path('products/create' ,ProductCreate.as_view(), name= "product_create"),
    path('products/<int:pk>', ProductDetail.as_view(), name= "product_detail"),
    path('products/<int:pk>/update', ProductUpdate.as_view(), name= "product_update"),
    path('products/<int:pk>/delete', ProductDelete.as_view(), name= "product_delete"),
    
]


