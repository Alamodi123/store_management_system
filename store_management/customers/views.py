from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer , UserRegisterSerializer
from rest_framework import generics



class CustomerRegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class CustomerList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CustomerDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class CustomerUpdate(generics.UpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class CustomerDelete(generics.DestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class CustomerRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
	

class CustomerRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer