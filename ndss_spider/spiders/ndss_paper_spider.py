# -*- coding: utf-8 -*-
import scrapy
from ndss_spider.items import NdssSpiderItem


class NdssPaperSpiderSpider(scrapy.Spider):
    name = 'ndss_paper_spider'
    allowed_domains = ['www.ndss-symposium.org', 'wp.internetsociety.org']
    start_urls = ['https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/']
    
    # def __init__(self):
    #     # self.item = []
    #     pass 
    def parse(self, response):
        # self.item = NdssSpiderItem()
        sels = response.xpath("//h3/a[@rel]")
        # print(sels)
        self.logger.warning("一共有{0}篇文章待下载".format(len(sels)))
        for sel in sels:
            title = sel.xpath("text()").extract()
            paper = sel.xpath("@href").extract()
            # self.logger.warning("new item: %s" % self.item)
            # yield(item)
            print("下载页面", paper[0])
            yield scrapy.Request(str(paper[0]), callback=self.get_download_page)
        
    def get_download_page(self, response):
        self.logger.warning("下载页面2")
        try:
            item = NdssSpiderItem()
            item['pdf'] = response.xpath("//p[@class='ndss_downloads']/a/@href")[0].extract()
            # try:
            #     item['slide'] = response.xpath("//p[@class='ndss_additional']/a/@href")[0].extract()
            # except Exception:
            #     item['slide'] = ''
            # try:
            #     item['video'] = response.xpath("//p[@class='ndss_additional']/a/@href")[1].extract()
            # except Exception:
            #     item['video'] = ''

            # 更换过滤方式
            item['slide'] = ''
            item['video'] = ''

            try:
                links = response.xpath("//p[@class='ndss_additional']/a")
                for link in links:
                    if link.xpath("text()")[0].extract() == 'Slides':
                        item['slide'] = link.xpath("@href")[0].extract()
                    elif link.xpath("text()")[0].extract() == 'Video':
                        item['video'] = link.xpath("@href")[0].extract()
            except Exception:
                self.logger.warning("此演讲没有可用的Slides和Video")

            self.logger.warning("重要信息:", item)
            yield item

        except Exception:
            self.logger.warning("此链接无法下载", response.xpath("//title/text()")[0].extract())

