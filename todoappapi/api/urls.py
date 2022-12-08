from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers




router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
router.register('todo', views.ToDoViewSets, basename='todo')
router.register('register', views.RegisterUserAPIView, basename='register')
router.register('logout/', views.RegisterUserAPIView, basename='logout')



urlpatterns = [
    path('', include(router.urls))
]