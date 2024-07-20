from django.db import models
from django.contrib.auth.models import User

class CitySearch(models.Model):
    city = models.CharField(max_length=100)
    search_count = models.IntegerField(default=0)
    last_searched = models.DateTimeField(auto_now=True)


