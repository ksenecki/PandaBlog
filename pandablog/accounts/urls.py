from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]