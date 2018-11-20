import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls= ["https://brickset.com/sets/year-2016"]


