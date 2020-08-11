# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random

class MiddleproDownloaderMiddleware:
    #拦截请求
    user_aget_list=['User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
]
    def process_request(self, request, spider):
        #UA伪装
        request.headers['User-Agent']=random.choice(self.user_aget_list)
        #request.meta['proxy'] ='http://171.35.163.80:9999'
        return None

    # 拦截响应
    def process_response(self, request, response, spider):
        # Called with the response returned sfrom the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response
    # 拦截发生异常请求
    PROXY_HTTP=[]
    PROXY_HTTPS = ['113.116.182.247:8088','14.115.104.46:808']
    def process_exception(self, request, exception, spider):
        #代理
        if request.url.split(':')[0]=='http':
            request.meta['proxy']='http://'+random.choice(self.PROXY_HTTP)
        else:
            request.meta['proxy'] = 'https://' + random.choice(self.PROXY_HTTPS)
        return request#将修正之后的请求对象重新请求发送