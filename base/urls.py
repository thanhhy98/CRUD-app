from django import http
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.webForm, name="home"),
    path('login/', views.loginUser, name="login"),
    path('delete/<str:pk>', views.deleteGoods, name="delete"),
    path('update/<str:pk>', views.updateGood, name="update"),
    path('logout/', views.logOut, name="logout"),
    path('search/', views.searchGood, name="search"),

]
