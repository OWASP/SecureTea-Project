from curses.ascii import US
from urllib.parse import uses_fragment
from django.http import HttpRequest, HttpResponse
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

@api_view(['post'])
def test(request):
    req_data = request.data
    users = User.objects.all()
    user = list(users.filter(cookie=req_data["cookie"]))
    print(user)
    if user:
        return Response(True)
    else:
        return Response(False)



@api_view(['POST'])
def login(request):
    """
    If user exists, Set a cookie to log in
    """
    req_data = request.data

    users = User.objects.all()
    # serializer = UserSerializer(users, many=True)
    user = list(users.filter(username=req_data["username"], password=req_data["password"]))
    if user:
        user = user[0]
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        user_data = UserSerializer(user).data
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        cookie_string = bytes(user_data["username"] + date_time, 'utf-8')
        cookie_string = hashlib.sha256(cookie_string).hexdigest()
        user.cookie = cookie_string
        user.save()

        return Response(cookie_string)

    else:
        print("Incorrect Credentials")
        return Response(False)

def is_logged_in(request):
    """
    checks if the cookie value is present in the databse. If present, User is logged in.
    """
    req_data = request.data
    users = User.objects.all()
    user = list(users.filter(cookie=req_data["cookie"]))[0]
    print(user)
    if user:
        return True
    else:
        return False

    

@api_view(['POST'])
def register(request):
    """
    Register new user
    """
    req_data = request.data

    users = User.objects.all()
    user = list(users.filter(username=req_data["username"]))
    if user:
        return Response(False) #if username exists, return False
    else:
        store_corporate = User(username=req_data["username"], password=req_data["password"])
        store_corporate.save()
        return Response(True)