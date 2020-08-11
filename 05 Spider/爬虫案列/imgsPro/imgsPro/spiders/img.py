import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        img_list=response.xpath('//*[@id="container"]/div')
        for img in img_list:
            # 注意：使用伪属性
            img_url=img.xpath('./div/a/img/@src2').extract_first()
            item=ImgsproItem()
            item['src']=img_url
            yield item
