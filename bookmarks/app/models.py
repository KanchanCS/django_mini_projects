from django.db import models

# Create your models here.
class Bookmarks(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    createdate = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    