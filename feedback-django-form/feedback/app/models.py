from django.contrib.auth.models import User
from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=30)
    rating = models.FloatField()  # validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    feed_data = models.TextField()
