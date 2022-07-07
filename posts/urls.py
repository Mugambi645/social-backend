from django.urls import path
from . import views
app_name = "posts"

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('/posts', views.getPosts, name='posts')
]
