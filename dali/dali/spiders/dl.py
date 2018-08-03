# -*- coding: utf-8 -*-
import scrapy


class DlSpider(scrapy.Spider):
    name = 'dl'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/s?ie=utf-8&wd=ip']

    def parse(self, response):
        with open('daili-ip.html','w',encoding='utf-8') as f:
            f.write(response.text)
