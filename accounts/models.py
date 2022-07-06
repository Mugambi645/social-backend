from django.db import models
import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        """create_user

        Args:
            name (string): name of the user
            email (email): email of the user
            password (_type_, optional): Password. Defaults to None.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            name=name,
            email=self.normalize_email(email)

        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, name, email, password=None):
        """
        Creates and saves a superuser with the given email, name
         and password.
        """
        user = self.create_user(
            email,
            password=password,
            name = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255,unique=True,)
    bio = models.CharField(max_length=255)
    image = models.ImageField(upload_to="account_images", blank=True, null=True)
    #is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email', 'password']

    def __str__(self):
        return self.name + " " + self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin