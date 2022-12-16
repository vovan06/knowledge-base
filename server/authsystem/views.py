from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserManager
from .models import User
from .serializers import CatalogSerializer


class UserManagerAPIView(APIView):
    def get(self, request):
        lst = UserManager.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = UserManager.objects.create(
            user=request.data['user']
        )
        return Response({'post': model_to_dict(post_new)})

class UserAPIView(APIView):
    def get(self, request):
        lst = User.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = User.objects.create(
            name=request.data['name'],
            middlename=request.data['middlename'],
            surname=request.data['surname'],
            department=request.data['department'],
            email=request.data['email'],
            private_access=request.data['private_access'],
            is_active=request.data['is_active'],
            is_staff=request.data['is_staff'],
            is_superuser=request.data['user']
        )
        return Response({'post': model_to_dict(post_new)})