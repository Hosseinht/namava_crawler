from asgiref.sync import sync_to_async
from django.db import transaction

from namava.models import Movie, Genre, Image


class CrawlerPipeline:
    def process_item(self, item, spider):
        return item


class MoviePipline(object):
    """
    This class process item object and save it to database
    """

    @sync_to_async
    @transaction.atomic
    def process_item(self, item, spider):
        genre_names = item.get("genre", [])

        genres = []
        for name in genre_names:
            genre, created = Genre.objects.get_or_create(name=name)
            genres.append(genre)

        movie = Movie.objects.create(
            title=item["title"],
            summary=item["summary"],
            release_year=item["release_year"],
            rate=item["rate"],
            duration=item["duration"],
        )

        # Add genres to the movie
        for genre in genres:
            movie.genre.add(genre)

        return item
