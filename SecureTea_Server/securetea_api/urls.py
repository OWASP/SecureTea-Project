from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('login/', views.login),
    path('register/', views.register)
    
]
