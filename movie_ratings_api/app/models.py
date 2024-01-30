from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256)
    rating = models.FloatField(null=True, default=None)

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="rating_movie")
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])