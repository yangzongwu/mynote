import scrapy

class MiddleSpider(scrapy.Spider):
    name = 'middle'
    start_urls = ['http://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=d6faf586000b8b7a&ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip&oq=ip&rsv_pq=d6faf586000b8b7a&rsv_t=ef4fEha%2Fn3pFF%2FTWFJVJV%2F3CvrKmCz1NbE5P4odN6naUCnWAAADI8IOoP9w&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&bs=ip&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=2&_cr1=24286']
    def parse(self, response):
        #page_text=response.text()
        page_text=response.xpath('/html').extract_first()
        with open('ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
