from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    """
    Model for storing post data
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #return a string of the class object
    def __str__(self):
        return self.user + " " + self.title
    