# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from testthree.items import TestthreeItem

class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['10jqka.com.cn']
    start_urls = ['http://q.10jqka.com.cn/thshy/']

    rules = (
        Rule(LinkExtractor(allow=('http://q.10jqka.com.cn/thshy/detail/code'),restrict_xpaths='//*[@id="maincont"]/table/tbody/tr/td[2]/a'),
             callback='parse_scomurl', follow=True),
        # Rule(LinkExtractor(restrict_xpaths='//*[@class="changePage"]'),callback='parse_item'),
    )

    def parse_scomurl(self, response):
        print(response.headers)
        # rules = (
        #     Rule(LinkExtractor(allow=('http://stockpagetext.10jqka.com.cn/')).extract_links(response),callback='parse_scomcode', follow=True),
        #     # Rule(LinkExtractor(restrict_xpaths='//*[@class="changePage"]'), callback='parse_item'),
        # )
    #     item=TestthreeItem()
    #     item['category']=response.text
    #     urls = LinkExtractor(allow=('http://stockpage.10jqka.com.cn/'),restrict_xpaths='// *[ @ id = "maincont"]/table/tbody/tr/ td[3] / a').extract_links(response)
    #     for  urldata in urls:
    #         item['scomname'] = urldata.text
    #         request = scrapy.Request(urldata.url, callback=self.parse_scomcode)
    #
    #         request.meta['item'] = item
    #         yield request
    #
    #
    #
    # def parse_scomcode(self,response):
    #     item = response.meta['item']
    #     item['scomcode']=response.url.split('/')[-1]
    #     yield item