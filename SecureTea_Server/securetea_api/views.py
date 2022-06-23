from urllib.parse import uses_fragment
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import User
from .serializers import UserSerializer

from datetime import datetime
import hashlib
# Create your views here.

"""

{
"username": "fox",
"password": "1234"
}

"""

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    # serializer = UserSerializer(users, many=True)
    # userdict = serializer.data
    # print(userdict)
    userlist = list(users.filter(username="Fox"))
    print(userlist)
    if userlist:
        user = UserSerializer(userlist, many=True).data
        print(user)
        return Response(True)
    else:
        print("User Doesn't Exist")
        return Response(False)

@api_view(['POST'])
def login(request):
    req_serializer  = UserSerializer(request.data)
    print(req_serializer.data)

    users = User.objects.all()
    # serializer = UserSerializer(users, many=True)
    userlist = list(users.filter(username=req_serializer.data["username"], password=req_serializer.data["password"]))
    print(userlist)

    now = datetime.now()
    date_time = now.strftime("%m%d%Y%H%M%S")
    print("date and time:",date_time)	

    if userlist:
        user = UserSerializer(userlist, many=True).data
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        cookie_string = bytes(user[0]["username"] + date_time, 'utf-8')
        cookie_string = hashlib.sha256(cookie_string).hexdigest()
        return Response(cookie_string)
    else:
        print("Incorrect Credentials")
        return Response(False)


def is_logged_in(request):
    pass

@api_view(['POST'])
def addUser(request):
    serializer  = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)