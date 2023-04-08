from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=500)
    release_year = models.SmallIntegerField()
    rate = models.SmallIntegerField()
    duration = models.SmallIntegerField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.movie.title
