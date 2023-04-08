# Scrape Namava api

## Installation

```bash
  git clone git@github.com:Hosseinht/namava_crawler.git && cd namava_crawler
```
```bash
  pip install -re requirements.txt
```
```bash
  python manage.py migrate
```
```bash
  python manage.py createsuperuser
```
```bash
  python manage.py runserver
```

## Run the crawler
```bash
  scrapy crawl namava
```
**now you can check the admin panel and see the scraped data**