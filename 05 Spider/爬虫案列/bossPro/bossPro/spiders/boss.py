import scrapy
from 爬虫案列.bossPro.bossPro import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/']
    urls='https://www.zhipin.com/c100010000/?page=%d'
    page_num=2

    def parse_detail(self,response):
        item=response.meta['item']
        job_desc=response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div').extract()
        job_desc=''.join(job_desc)
        item['job_desc']=job_desc
        yield item

    def parse(self, response):
        job_list=response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in job_list:
            item=BossproItem()
            job_name=li.xpath('./div/a/p/span/text()').extract_first()
            item['job_name']=job_name
            detail_url='https://www.zhipin.com'+li.xpath('./div/a/@href').extract_first()
            #请求传参 meta={}，可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num<=3:
            new_url=format(self.urls%self.page_num)
            self.page_num+=1
            yield scrapy.Request(new_url,callback=self.parse)