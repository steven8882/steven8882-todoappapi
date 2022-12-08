from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.utils.regex_helper import contains
from .serializers import RegisterSerializer, ToDoSerializer, UserSerializer
from rest_framework import fields, serializers, viewsets
from .models import ToDos
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view
from django.forms import ModelForm
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from knox.models import AuthToken
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.utils.timezone import now
from django.utils import timezone
from rest_framework import filters
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView


class ToDoViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ToDos.objects.all()
    serializer_class = ToDoSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    search_fields= ['title','desc']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return ToDos.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # request.data[] = 
        print(request.data)
        ser = self.serializer_class(data=request.data)
        ser.is_valid()
        print(ser.errors)  # force to show errors
        return super().create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        print(serializer.errors)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(["GET"])
def logOutUser(request):
    logout(request)
    return Response({
        "logout": "success"

    })


class RegisterUserAPIView(viewsets.ModelViewSet):
  permission_classes = (AllowAny,)
  queryset = ''

  serializer_class = RegisterSerializer


