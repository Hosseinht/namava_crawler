import os
import shutil
from io import BytesIO

import requests
from asgiref.sync import sync_to_async
from django.conf import settings
from django.db import transaction
from PIL import Image as PILImage
from scrapy.exceptions import DropItem

from namava.models import Genre, Image, Movie


class CrawlerPipeline:
    def process_item(self, item, spider):
        return item


class MoviePipline(object):
    """
    This class process item object and save it to database
    """

    def __init__(self):
        self.image_urls = set()
        # downloaded images go to this empty set. so we can keep track
        # of the images and avoid downloading the same image

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

        if "image_urls" in item:
            for image_url in item["image_urls"]:
                # Check if the image has already been downloaded
                if image_url in self.image_urls:
                    continue
                    # if image exist skip the loop and go to the other image
                self.image_urls.add(image_url)

                # Download the image
                response = requests.get(image_url)
                if response.status_code != 200:
                    raise DropItem("Failed to download image")

                # Open the image using PIL and put it in the memory
                image = PILImage.open(BytesIO(response.content))

                # Create a directory for images if directory does not exist
                directory = os.path.join(settings.MEDIA_ROOT, f"{movie.id}")
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Save the image
                filename = os.path.basename(image_url)
                image_path = os.path.join(directory, filename)
                with open(image_path, "wb") as f:
                    image.save(f)

                # Create Image object and link it to the movie
                Image.objects.create(image=image_path, movie=movie)

                # Delete the folder that scrapy create for downloaded images
                image_dir = "media/full"
                if os.path.exists(image_dir):
                    shutil.rmtree(image_dir)
        return item
