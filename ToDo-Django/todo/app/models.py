import re
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.

class  UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,  email, password=None, **extra_fileds):

        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, email, password, **extra_fileds):
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_superuser', True)
        extra_fileds.setdefault('is_active', True)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError(("Superuser is must have a staff true"))
        return self.create_user(email, password, **extra_fileds)

class Account(AbstractUser):
    username = None
    GENDER = (
        ('Male', "Male"),
        ('Female', "Female")
    )
    phone = models.CharField(max_length=10 , blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, choices=GENDER , default='Mail')


    objects = UserManager()
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


