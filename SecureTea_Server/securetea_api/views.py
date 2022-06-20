from configparser import InterpolationMissingOptionError
import imp
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    items = User.objects.all()
    serializer = UserSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer  = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
    return response(serializer.data)