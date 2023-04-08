import json
import scrapy
from scrapy.loader import ItemLoader
from crawler.items import MovieItem, ImageItem


class NamavaSpider(scrapy.Spider):
    name = "namava"
    allowed_domains = ["namava.ir"]
    start_urls = ["https://www.namava.ir/api/v1.0/medias/latest/?pi=1&ps=30"]

    def parse(self, response):
        """
        parse method is responsible for handling the response that comes from start_urls.

        scrapy.Request send a request to the url and the callback function(parse_movie) that is responsible
         for handling the response
        """

        resp = json.loads(response.body)

        for media in resp["result"]:
            if media["type"] == "Movie":
                yield scrapy.Request(
                    f"https://www.namava.ir/api/v2.0/medias/{media['id']}/single-movie",
                    callback=self.parse_movie,
                )

    def parse_movie(self, response):
        resp = json.loads(response.body)
        result = resp["result"]
        images = json.loads(result["slide"])

        movie_images = []
        for image in images:
            # get all the images of a movie and change their relative urls to absolute urls
            image = image["Url"]
            image = f"https://static.namava.ir{image}"
            movie_images.append(image)

        category_names = [category["categoryName"] for category in result["categories"]]

        item = MovieItem()

        item["title"] = result["caption"]
        item["summary"] = result["story"]
        item["release_year"] = result["year"]
        item["rate"] = result["hit"]
        item["duration"] = result["mediaDuration"]
        item["genre"] = category_names
        # item['images'] = movie_images,

        yield item

