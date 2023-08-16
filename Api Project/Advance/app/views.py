from imaplib import _Authenticator
from urllib import response
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from app.models import Flipkart_Api

from app.serializer import Flipkart_ApiSerializers, LoginSerializers
# from app.serializers import LoginSerializers

# Create api for Login view

class LoginApi(APIView):
    
    def post(self,request):
        try:
            data = request.data
            serializer = LoginSerializers(data=data)
            if serializer.is_valid():
                email=serializer.data['email']
                password=serializer.data['password']
                
                user=_Authenticator(email = email,password = password)
                
                if user is None:
                    
                    return response({
                        'status' : 400,
                        'message' : 'invalid password',
                        'data' : {}
                    })
                    
                refresh = RefreshToken.for_user(user)
                return response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    })
                    
                
            return response({
                'status' : 400,
                'message' : 'something went wrong',
                'data' : serializer.errors
            })
        
        except Exception as e:
            print(e)
   
# This is for flipkart views.          
class Flipkart_ApiViewset(viewsets.ModelViewSet):
    queryset = Flipkart_Api.objects.all()
    serializer_class = Flipkart_ApiSerializers
