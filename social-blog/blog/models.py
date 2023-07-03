import datetime as dt


from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    caption = models.CharField(max_length=65)
    content = models.TextField(blank=True)
    upload_file = models.FileField(
        upload_to="videos",
        blank=True,
        validators=[FileExtensionValidator(["mp4", "jpeg", "png", "jpg"])],
    )
    create_date = models.DateTimeField(default=dt.datetime.now)
    updated_date = models.DateTimeField(default=dt.datetime.now)

    def __str__(self):
        return self.name


class FollowedPerson(models.Model):
    person = models.ForeignKey(User, related_name="person", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=dt.datetime.now)

    class Meta:
        unique_together = (("person", "user"),)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = self.post.name + " liked by " + self.user.username
        return result
