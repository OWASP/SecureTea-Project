from urllib.parse import uses_fragment
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    userdict = serializer.data
    print(userdict)
    """
    for dict in userdict:
        for key,value in dict.items():
            if (key == 'username')
            print(key)
            print(value)
        print("\n")
    """
    b = users.filter(username="Fox1000")
    print(b)
    
    
    return Response(userdict)

@api_view(['POST'])
def addUser(request):
    serializer  = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)