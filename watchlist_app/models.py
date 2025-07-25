
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.timezone import activate
from rest_framework.fields import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length = 20)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length = 100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length = 300)
    platform = models.ForeignKey(StreamPlatform , on_delete=models.CASCADE , related_name="watchlist")
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User , on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
    description = models.TextField(max_length=300 , null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    watchlist = models.ForeignKey(WatchList , on_delete=models.CASCADE, related_name = "reviews")


    def __str__(self):
        return str(self.rating) + "-" + self.watchlist.title
