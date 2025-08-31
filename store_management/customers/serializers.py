from rest_framework import serializers                 # Import DRF serializers (convert data -> JSON and back)
from .models import User                               # Import our custom User model                      
from django.contrib.auth.password_validation import validate_password  # Built-in password validator


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["id","username","email"]
          
# Serializer for registering a new user
class UserRegisterSerializer(serializers.ModelSerializer):
    # Ask for password (only for writing, never shown back)
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password],style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True,style={'input_type': 'password'} )
   # Can only be sent, not returned in responses # Must be provided # Check password strength (Django rules)

    class Meta:
        model = User  # Connect serializer to our User model
        fields = ('username', 'email', 'password', 'password2', 'role')  
        # These are the fields we need when registering

    # Custom validation: check if both passwords match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    # How to create a new User object from the validated data
    def create(self, validated_data):

        # Create the user without saving the raw password
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )

        # Set the password the safe way (hashing it)
        user.set_password(validated_data['password'])
        user.save()
        return user



# from rest_framework import serializers
# from .models import User
# from django.contrib.auth.password_validation import validate_password 

# class RegisterSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ["username","email","password"]
		

		

