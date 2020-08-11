import scrapy
from qiubaiPro.items import QiubaiproItem

class SpidernameSpider(scrapy.Spider):
    name = 'spiderName'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            author=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content=div.xpath('./a[1]/div/span//text()').extract()
            content=''.join(content)
            item=QiubaiproItem()
            item['author']=author
            item['content']=content
            yield item#将item提交给了管道
