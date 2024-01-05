from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import Token,TokenError,RefreshToken



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6,write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6,write_only=True)
    
    class Meta:
        model = User
        fields = ["name","gender","email","phone_number","instagram","location","password","password2","category","experience","unique_code"]
        extra_kwargs = {
            'password':{
                'write_only':True
            },

            
        }
        
    def validate(self, data):
        # Check if passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")

        return data
        
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', None)
        if password and password2 and password == password2:
            # If both passwords match, set the hashed password
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            return user

        raise ValidationError("Passwords do not match or are missing")
 