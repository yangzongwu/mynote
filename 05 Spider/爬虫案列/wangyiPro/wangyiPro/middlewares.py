# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep
class WangyiproDownloaderMiddleware:
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):#spider爬虫对象
        bro=spider.bro
        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response
        if request.url in spider.models_urls:#五大版本对应的响应对象
            bro.get(request.url)
            sleep(1)
            page_text=bro.page_source
            #针对定位到的这些response进行篡改
            #实例化一个新的响应对象（包含动态加载出来的数据）
            new_response=HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:#其他响应对象
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
