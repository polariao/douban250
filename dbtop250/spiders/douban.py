# -*- coding: utf-8 -*-
import scrapy
from dbtop250.items import Dbtop250Item
from scrapy import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    #设置浏览器用户代理
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    def start_requests(self):
        return [Request("https://movie.douban.com/top250?start=0&filter=", headers=self.header)]
   # start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    m=1
    def parse(self, response):
        print('第'+str(self.m)+'页')
        self.m += 1
        item = Dbtop250Item()
        item['url'] = response.xpath('//div[@class="hd"]/a/@href').extract()
        #获取相应链接
        for j in range(0, len(item['url'])):
            #对或得到的链接进行爬取
            yield Request(item['url'][j], callback=self.return_pass, headers=self.header)
        #抓取其他页面
        for i in range(1, 10):
            url = "https://movie.douban.com/top250?start=" + str(i*25) + "&filter="
            yield Request(url, callback=self.parse,headers=self.header)

    def return_pass(self,response):
        item = Dbtop250Item()
        item['title'] = response.xpath('/html/head/title/text()').extract()   #电影名
        item['director'] = response.xpath("//span[@class='attrs']/a[@rel='v:directedBy']/text()").extract()   #导演
        item['content'] = response.xpath('//span[@property="v:summary"]/text()').extract()  #简介
        item['time'] = response.xpath('//span[@property="v:runtime"]/text()').extract()  #电影时长
        item['image'] = response.xpath('//img[@rel="v:image"]/@src').extract()   #封页
        yield item
