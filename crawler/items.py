import scrapy
from scrapy_djangoitem import DjangoItem

from namava.models import Movie


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(DjangoItem):
    """
    Data that spider extract and parsed will come here to create an instance of Movie.
    It simply maps scraped data to Django model
    """

    django_model = Movie
    genre = scrapy.Field()
    cast = scrapy.Field()
    image_urls = scrapy.Field()
