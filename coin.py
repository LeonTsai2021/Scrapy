# -*- coding: utf-8 -*-
import scrapy


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['web.archive.org/web/20200116052415/https://www.livecoin.net/en/']
    start_urls = ['http://web.archive.org/web/20200116052415/https://www.livecoin.net/en//']

    def parse(self, response):
        pass
