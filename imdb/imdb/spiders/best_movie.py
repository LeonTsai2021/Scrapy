# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMovieSpider(CrawlSpider):
    name = 'best_movie'
    allowed_domains = ['web.archive.org']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    def start_requests(self):
        yield scrapy.Request(url='http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            'User-Agent': self.user_agent
        })
   
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//h3[@class="lister-item-header"]/a')), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=('(//a[@class="lister-page-next next-page"])[2]'), process_request='set_user_agent'))
    )

    def parse_item(self, response):
        yield{
            'title':response.xpath('//div[@class="title_wrapper"]/h1/text()').get(),
            'year':response.xpath('//span[@id="titleYear"]/a/text()').get(),
            'duration':response.xpath('normalize-space((//time)[1]/text())').get(),
            'genre':response.xpath('//div[@class="subtext"]/a[1]/text()').get(),
            'rating':response.xpath('//div[@class="ratingValue"]/strong/span/text()').get(),
            'movie_url':response.url
        }