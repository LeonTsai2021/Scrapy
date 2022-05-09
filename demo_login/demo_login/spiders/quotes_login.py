# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest

class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['quotes.toscrape.com/login']
    start_urls = ['https://quotes.toscrape.com/login/']

    def parse(self, response):
        csrf_token = response.xpath('//input[@name="csrf_token"]/@value').get()
