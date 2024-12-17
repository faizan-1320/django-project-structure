from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from project.users.models import User
from .serializers import UserSerializer,UserLoginSerilizer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.
class UserRegister(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'User Register Successfullly!'},status=status.HTTP_201_CREATED)
    
class UserLogin(APIView):
    def post(self,request):
        serializer = UserLoginSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data.get('username'), password=serializer.validated_data.get('password'))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'Token':token.key},status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=400)