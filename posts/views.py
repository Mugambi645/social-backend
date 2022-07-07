from django.shortcuts import render
from rest_framework import Response
from .models import Post
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    
    routes = [

    ]

    return Response(routes)


@api_view(['GET'])
def getPosts(request):
    return Response('NOTES')
