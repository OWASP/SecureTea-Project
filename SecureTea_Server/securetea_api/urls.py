from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.getData),
    path('add/', views.addUser),
    path('login/', views.login),
    
]
