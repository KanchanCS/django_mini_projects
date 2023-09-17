from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    create_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish = models.BooleanField(default  = True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)    
    
    def __str__(self):
        return self.title