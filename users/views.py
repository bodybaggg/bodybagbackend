from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User,CategoryName
from rest_framework import status
from .communitycode import generate_unique_code#, post_save_generate_unique_code
import jwt,datetime
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
       
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.is_active = True
            user.save()
            unique_code = user.unique_code
            if not unique_code:
                generate_unique_code(sender=User, instance=user,created=True)
                user.refresh_from_db()
                unique_code = user.unique_code
            
            #Generate JWT token
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload,'secret', algorithm='HS256')
            
            return Response({
                "CommunityCode":unique_code,
                'jwt':token
                },
                            status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
 
class LoginUserView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256')
        
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data = {
        
                         'message':'Success',
                         'jwt':token
                         
        }
        
        return response

class ViewProfile(APIView):
    
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")
        user = User.objects.filter(id =payload['id']).first()
        
        serializer = UserSerializer(user)
        
        response = Response()
        response.data = {
            'username': serializer.data['name'],
            'CommunityCode': serializer.data['unique_code']
        }
        return response
        
        
class LogoutView(APIView):
    def post(self,request):
        response =Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'Logout Success'
        }
        
        return response
    
    
class CategoryList(APIView):

    def get(self, request):
        Categories = CategoryName.objects.all()
        serializer = CategorySerializer(Categories, many=True)
        return Response(serializer.data)
        
