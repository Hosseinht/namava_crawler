from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    release_year = models.SmallIntegerField(
        validators=[MinValueValidator(1300), MaxValueValidator(1500)]
    )
    rate = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    duration = models.SmallIntegerField()
    genre = models.ManyToManyField(Genre)
    image = models.ImageField()

    def __str__(self):
        return self.title