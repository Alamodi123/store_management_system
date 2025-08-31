from django.urls import path , include 
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),  
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), 
    
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    #path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_details'),
    #path('customers/<int:pk>/update', CustomerUpdate.as_view(), name='customer_update'),
    #path('customers/<int:pk>/delete', CustomerDelete.as_view(), name='customer_delete'),
    path('customers/<int:pk>/', CustomerRUD.as_view(), name='customer_rud'),

]