# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']

    def start_requests(self):
        yield scrapy.Request(url='https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html',callback=self.parse,headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
        })
        
    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield{
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discount_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'origin_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
            }

        next_page=response.xpath("//a[@class='nextPage']/@href").get()
        
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse,headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
            })