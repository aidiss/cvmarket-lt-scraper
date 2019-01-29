# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MainSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['cvmarket.lt']
    start_urls = ['https://www.cvmarket.lt/kaunas']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= '//a[@class="f_job_title main_job_link"]'), callback='parse_listing', follow=True),
        Rule(LinkExtractor(allow='imones-darbo-skelbimai-'), callback='parse_company', follow=True)
    )

    
    def parse_listing(self, response: scrapy.http.Response):
        i = {}
        i['url'] = response.url
        i['expire'] = response.xpath('//a[@class="expire"]/span/text()').extract_first()
        i['job-title'] = response.css('span#main-job-title  *::text').extract()
        i['main'] = response.css('div#main-lang-block *::text').extract()
        i['job-details'] = response.css('div.jobdetails *::text').extract()
        return i

    def parse_company(self, response: scrapy.http.Response):
        i = {}
        i['content-wrapper'] = response.css('.content-wrapper::text')
        # return i
