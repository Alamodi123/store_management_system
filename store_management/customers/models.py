from django.contrib.auth.models import AbstractUser   # Import Django's built-in User model (with username, password, email, etc.)
from django.db import models                          # Import models to create database tables

# Custom User model (extends the default Django User)
class User(AbstractUser):
    # Define the roles that a user can have
    ROLE_CHOICES = (
        ('customer', 'Customer'),   # Option 1: Customer
        ('staff', 'Staff'),         # Option 2: Staff
    )

    # Add a 'role' field to the user
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='customer')

    # This makes the username show up nicely when printing the object
    def __str__(self):
        return self.username
