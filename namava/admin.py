from django.contrib import admin

from .models import Cast, Genre, Image, Movie


class MovieImageInline(admin.TabularInline):
    model = Image


class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieImageInline]


admin.site.register(Cast)
admin.site.register(Genre)
admin.site.register(Image)
admin.site.register(Movie, MovieAdmin)
