from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    
    routes = [

    ]

    return Response(routes)


@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
