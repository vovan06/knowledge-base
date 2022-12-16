from django. forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Catalog
from . models import Document
from .serializers import CatalogSerializer
class CatalogAPIView(APIView):
    def get (self, request):
        lst = Catalog.objects.all().values ()
        return Response ({'posts': list(lst)})

    def post (self, request):
        post_new = Catalog.objects .create(
            title=request. data['title']
        )
        return Response ({'post': model_to_dict(post_new)})

class DocumentAPIView(APIView):
    def get (self, request):
        lst = Document.objects.all().values ()
        return Response ({'posts': list(lst)})



    def post (self, request):
        post_new = Document.objects .create(
            title=request. data['title'],
            file=request. data[ 'file'],
            private_access=request.data['private_access'],
            created_at=request.data['created_at'],
            catalog=request.data['catalog'],
        )
        return Response ({'post': model_to_dict(post_new)})