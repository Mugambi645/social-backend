from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    """
    Model for storing post data
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    #return a string of the class object
    def __str__(self):
        return self.user + " " + self.title

class Comment(models.Model):
    """comment model

    Args:
        models (class): model to create comments
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.post + "" + self.body