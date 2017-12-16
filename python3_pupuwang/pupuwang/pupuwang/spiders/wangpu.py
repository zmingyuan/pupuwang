# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pupuwang.items import PupuwangItem

class WangpuSpider(CrawlSpider):
    name = 'wangpu'
    allowed_domains = ['sh.pupuwang.com']
    # 爬取“找店选址”所有信息
    start_urls = ['http://sh.pupuwang.com/qzqg/']

    # 定义提取规则
    rules = (
        # 列表页
        Rule(LinkExtractor(allow=(r'all')),follow=True),
        # 详情页
        Rule(LinkExtractor(allow=(r'details/\d+')),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        item = PupuwangItem()
        title = response.xpath('//div[@class="opportunity-title"]/text()').extract()[0].strip()
        url = response.url
        industry = response.xpath('//ul[@class="detail-detail"]//li[3]/div[1]/text()').extract()[0].strip()
        pubtime = response.xpath('//div[@class="shop-data"]//span[2]/text()').extract()[1].strip()
        size = response.xpath('//ul[@class="detail-detail"]//li[1]/div[1]/text()').extract()[0].strip()
        rent = response.xpath('//ul[@class="detail-detail"]//li[2]/div[1]/text()').extract()[0].strip()
        describe = response.xpath('//div[@class="Candicine-content-content"]/p/text()').extract()[0].strip()

        item['title'] = title
        item['url'] = url
        item['industry'] = industry
        item['pubtime'] = pubtime
        item['size'] = size
        item['rent'] = rent
        item['describe'] = describe

        yield item
