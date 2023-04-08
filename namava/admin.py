from django.contrib import admin
from .models import Genre, Movie, Image


class MovieImageInline(admin.TabularInline):
    model = Image


class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieImageInline]


admin.site.register(Genre)
admin.site.register(Image)
admin.site.register(Movie, MovieAdmin)
