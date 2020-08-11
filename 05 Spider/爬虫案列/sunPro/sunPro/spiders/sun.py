import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from 爬虫案列.sunPro.sunPro import SunproItem
class SunSpider(RedisCrawlSpider):
    name = 'sun'
    redis_key='pic'
    rules = (Rule(LinkExtractor(allow=r'list[0-9]*\.html'), callback='parse_item', follow=True),)
    conn=Redis(host='127.0.0.1',port=6379)
    def parse_item(self, response):
        li_list=response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            name=li.xpath('./a[2]/b/text()').extract_first()
            detail_url=li.xpath('./a[1]/@href').extract_first()
            ex=self.conn.sadd('urls',detail_url)
            if ex==1:
                yield scrapy.Request(url=detail_url,callback=self.parse_detail)
            else:
                print("already exist")
    def parse_detail(self,response):
        item=SunproItem()
        item['name']='xxx'
        item['detail']='xxx'
        yield item