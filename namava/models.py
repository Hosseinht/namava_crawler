from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    summary = models.TextField(max_length=500)
    release_year = models.SmallIntegerField()
    rate = models.SmallIntegerField()
    duration = models.SmallIntegerField()
    genre = models.ManyToManyField(Genre)
    cast = models.ManyToManyField(Cast)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title
