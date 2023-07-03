import datetime as dt

from django.db import models
from django.utils import timezone

# Create your models here.


class IndustrySummary(models.Model):
    topic = models.CharField(max_length=75)
    region = models.CharField(max_length=75, blank=True)
    sector = models.CharField(max_length=75, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pestle = models.CharField(max_length=100, blank=True)
    sources = models.CharField(max_length=100, blank=True)
    impact = models.CharField(max_length=75, blank=True)
    insight = models.CharField(max_length=200, blank=True)
    title = models.TextField(default="")
    url = models.URLField(blank=True)
    likelihood = models.IntegerField(default=0, null=True)
    relevance = models.IntegerField(default=0, null=True)
    intensity = models.IntegerField(default=0, null=True)
    start_year = models.DateField(null=True)
    end_year = models.DateField(null=True)
    add_date = models.DateTimeField(null=True)
    publish_date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        title = self.title
        return title[:50]

    def _get_year(self):
        return str(self.published_date.year)
