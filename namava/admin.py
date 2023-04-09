from django.contrib import admin
from django.utils.html import format_html

from .models import Cast, Genre, Image, Movie


class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_select_related = ["movie"]


class CastAdmin(admin.ModelAdmin):
    model = Cast

    search_fields = ["name"]


class MovieImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["thumbnail"]

    def thumbnail(self, instance):
        # create a thumbnail for images in the admin panel
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" width="120" height="100"/>'
            )
        return ""


class MovieAdmin(admin.ModelAdmin):
    search_fields = ["title", "director", "cast__name"]
    list_filter = ["director", "release_year", "genre"]
    list_display = ["title", "release_year", "director", "cast_names"]
    inlines = [MovieImageInline]
    filter_horizontal = ["cast", "genre"]

    def cast_names(self, obj):
        # display top 4 actors in the movie list in the admin panel
        return ", ".join([cast.name for cast in obj.cast.all()[:4]])

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("cast", "genre")


admin.site.register(Cast, CastAdmin)
admin.site.register(Genre)
admin.site.register(Image, ImageAdmin)
admin.site.register(Movie, MovieAdmin)
