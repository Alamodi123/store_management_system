from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics

class ProductList(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
     
class ProductCreate(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	
class ProductDetail(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
     
class ProductDelete(generics.DestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
      
class ProductUpdate(generics.UpdateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	
