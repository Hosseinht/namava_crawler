from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=500)
    release_year = models.SmallIntegerField()
    rate = models.SmallIntegerField()
    duration = models.SmallIntegerField()
    genre = models.ManyToManyField(Genre)

    # image = models.ImageField(null=True)

    def __str__(self):
        return self.title
