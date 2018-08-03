# -*- coding: utf-8 -*-
import json

import scrapy

class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['www.baidu.com']

    def start_requests(self):
        post_url='http://fanyi.baidu.com/sug'
        words='hello'
        data={
            'kw':words
        }
        # 提交post请求
        # url  post地址
        # formdata  post参数
        # headers   post请求头
        # callback  回调函数，引擎会把response对象回传给这个指定的函数
        yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.parse_info)

    # 自定义的函数，由callback指定的回调方法
    def parse_info(self, response):
        obj = json.loads(response.text, encoding='utf-8')
        string = json.dumps(obj, ensure_ascii=False)
        # 解析内容即可
        print(string)
