# scrapy框架
* 环境安装：
    * mac or linux: pip install scrapy
    * windows:
        * pip install wheel
        * pip install twisted
        * pip install pywin32
        * pip install scrapy
* 基本使用：
    * 创建一个工程：
        * scrapy startproject xxxPro
    * 在spiders 子目录中创建一个爬虫文件:
        * scrapy genspider spiderName www.xxx.com
    * 执行工程:
        * scrapy crawl spiderName
        
        
# scrapy 数据解析
```python
class SpidernameSpider(scrapy.Spider):
    name = 'spiderName'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #解析作者名称+段子内容
        div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            # Xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中data存储的字符串提取出来
            author=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            # 列表调用了extract之后，则表示将列表中每一个Selector对象中的data对象的字符串提取出来
            content=div.xpath('./a[1]/div/span//text()').extract()
            content=''.join(content)
            print(author,content)
```

# scrapy 持久化存储
* 基于终端指令
    * 只可以将parse方法的返回值存储到本地的文本文件中
    * 对应的文本文件类型固定('json', 'jsonlines', 'jl', 'csv', 
    'xml', 'marshal', 'pickle')
    ```python
    import scrapy
    class SpidernameSpider(scrapy.Spider):
        ...
        def parse(self, response):
            ...
            all_data=[]
            return all_data
    ```
    ```
    scrapy crawl spiderName -o./quibai.csv
    ```    
* 基于管道
    * 编码流程
        * 数据解析
        * 在item类中定义相关的属性
        * 将解析的数据封装存储到item类型的对象
        * 将item类型的对象提交给管道进行持久化存储的操作
        * 在管道类的process_item中要将其接收到的item对象中存储的数据进行持久化存储操作
        * 在配置文件中开启管道
    * 多个存储要求：
        * 在setting中选择优先级最高的管道类先进行存储
        * 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
        * process_item中return item 就会传递给下一个即将执行的管道类
        
### 持久化存储案例
###### 环境配置
* scrapy startproject xxxPro
* scrapy genspider spiderName www.xxx.com
* scrapy crawl spiderName
###### --spiderName.py--
```python
import scrapy
from items import QiubaiproItem
class SpidernameSpider(scrapy.Spider):
    name = 'spiderName'
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
```
###### --items.py--
```python
import scrapy
class QiubaiproItem(scrapy.Item):
    author=scrapy.Field()
    content=scrapy.Field()
```
###### --settings.py--
```python
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL='ERROR'
ITEM_PIPELINES = {
    'qiubaiPro.pipelines.QiubaiproPipeline': 300,
    'qiubaiPro.pipelines.mysqlPileLine': 301,
}
```
###### --pipelines.py--
```python
import pymysql
class QiubaiproPipeline:
    fp=None
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp=open('./qiubai.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        author=item['author']
        content=item['content']
        self.fp.write(author+':'+content)
        return item#传递给下一个即将执行的管道类
    def close_spider(self,spider):
        print("结束")
        self.fp.close()

class mysqlPileLine(object):
    conn=None
    cursor=None
    def open_spider(self,spider):
        self.conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='20110806',db='qiubai',charset='utf8')
    def process_item(self,item,spider):
        self.cursor=self.conn.cursor()
        try:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS qiubai1(author varchar(10),content varchar(500));')
            self.cursor.execute('use qiubai;')
            self.cursor.execute('insert into qiubai1 values("%s","%s");'%(item["author"],item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
```

# 全栈数据爬取
* 就是将网站中某板块下的全部页码对应的页面数据进行爬取
* 需求：爬取校花网中照片的名称
* 实现方式：
    * 将所有页面的url添加到当前的urls列表（不推荐）
    * 自行手动推荐请求发送
        ```python
        yield scrapy.Request(url=new_url,callback=self.parse)
        ```
###### --xiaohua.py--
```python
import scrapy
class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']
    
    url='http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num=2
    def parse(self, response):
        li_list=response.xpath('//div[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_name=li.xpath('./a[2]/text()|./a[2]/b/text()').extract_first()
            print(img_name)
        if self.page_num<=11:
            new_url=format(self.url%self.page_num)
            self.page_num+=1
            #手动callback回调函数用于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)
```

# 五大核心模块
* 引擎 Scrapy
* 调度器 Scheduler
* 下载器 Downloader
* 爬虫 Spider
* 项目管道 Pipeline

# 请求传参
* 使用场景：如果爬取解析的数据不在同一张页面中（深度爬取）
* 需求：爬取BOSS的岗位名称和岗位描述
```python
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
```

# 图片爬取ImagesPipeline
基于scrapy爬取的字符串类型的数据和爬取图片类型的数据区别？
* 字符串：只需要基于xpath进行解析且提交管道进行持久化存储
* 图片：xpath 解析出图片src的属性值。单独的对图片地址发起请求获取图片二进制类型的数据
* ImagesPipeline：
    * 只需要将img的src的属性值进行解析，提交到管道，管道就会对图片的srcj进行请求发送获取
    二进制类型的数据，且还会帮我们进行持久化存储
    * 需求：爬取站长素材高清图片
    * 使用流程
        * 数据解析：图片的地址
        * 将存储图片的地址的itemt提交到指定的管道类
        * 在管道文件中自定制一个基于ImagesPipeline的管道类
        * 配置文件中：
            * 指定图片存储的目录
            * 指定开启的管道类

### 案列
###### 环境配置
```
scrapy startproject imgPro
scrapy genspider spiderName www.xxx.com
scrapy crawl imgs
```
###### --img.py--
```python
import scrapy
from imgsPro import ImgsproItem
class ImgSpider(scrapy.Spider):
    name = 'img'
    start_urls = ['http://sc.chinaz.com/tupian/']
    def parse(self, response):
        img_list=response.xpath('//*[@id="container"]/div')
        for img in img_list:
            # 注意：使用伪属性
            img_url=img.xpath('./div/a/img/@src2').extract_first()
            item=ImgsproItem()
            item['src']=img_url
            yield item
```
###### --items.py--
```python
import scrapy
class ImgsproItem(scrapy.Item):
    src=scrapy.Field()
```
###### --pipelines.py--
```python
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class ImagePipeline(ImagesPipeline):
    #根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])
    #指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        img_name=request.url.split('/')[-1]
        return img_name
    #返回下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item
```
###### --settings.py--
```python
...
USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
ROBOTSTXT_OBEY = False
LOG_LEVEL='ERROR'
...
ITEM_PIPELINES = {
    'imgsPro.pipelines.ImagePipeline': 300,
}
...
# 指定图片存储的目录
IMAGES_STORE='./imgs'
```

# 中间件
* 爬虫中间件：引擎和Spider中间
* 下载中间件：引擎和下载器中间是
    * 作用：批量拦截到整个工程所有的请求和响应
    * 拦截请求：
        * UA伪装 process_request
        * 代理IP: return request
    * 拦截响应：
        * 篡改响应数据，响应对象
        
### 拦截请求
```python
import random
class MiddleproDownloaderMiddleware:
    #拦截请求
    user_aget_list=['User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
]
    def process_request(self, request, spider):
        #UA伪装
        request.headers['User-Agent']=random.choice(self.user_aget_list)
        request.meta['proxy'] ='http://171.35.163.80:9999'
        return None
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
```

### 拦截响应
需求：爬取网易新闻中新闻数据（标题和内容）
* 通过网易新闻的首页解析出五大板块对应的详情的url(没有动态加载)
* 每一个板块对应的新闻标题都是动态加载出来的(动态加载)
* 通过解析出每一条新闻详情页的url获取详情页面数据(非动态加载)
###### 环境配置
```
scrapy startproject wangyiPro
scrapy genspider wangyi www.xxx.com
scrapy crawl wangyi
```

###### --wangyi.py--
```python
import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    start_urls = ['https://news.163.com/']

    # 实例化一个浏览器对象
    def __init__(self):
        self.bro=webdriver.Chrome(executable_path='/爬虫案列/chromedriver.exe')

    models_urls=[]
    def parse(self, response):
        li_list=response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist=[3,4,6,7,8]
        for index in alist:
            model_url=li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        for url in self.models_urls:
            yield scrapy.Request(url,callback=self.parse_model)

    #解析每一个板块标题和详情页的url
    def parse_model(self,response):
        div_list=response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title=div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url=div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item=WangyiproItem()
            item['title']=title
            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        content=response.xpath('// *[ @ id = "content"]//text()').extract()
        content=''.join(content)
        item=response.meta['item']
        item['content']=content
        yield item

    def close(self, spider):
        self.bro.quit()
```
###### --items.py--
```python
import scrapy
class WangyiproItem(scrapy.Item):
    title=scrapy.Field()
    content=scrapy.Field()
```

###### --middlewares.py--
```python
from scrapy.http import HtmlResponse
from time import sleep
class WangyiproDownloaderMiddleware:
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
```
###### --pipelines.py--
```python
class WangyiproPipeline:
    def process_item(self, item, spider):
        print(item)
```


# Crawlspider 
* 是Spider一个子类，主要用于全站数据爬取
* 全站爬取方式：
    * 基于Spider:手动请求
    * 基于Crawlspider
* Crawlspider的使用：
    * 创建一个工程
    * cd XXX
    * 创建爬虫文件(Crawlspider)：
        * scrapy genspider -t crawl xxx www.xxx.com
        * 链接提取器:根据指定的规则进行指定的链接提取
        * 规则解析器：将连接提取器取到的链接进行指定规则（callback）的解析操作
```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class SunSpider(CrawlSpider):
    name = 'sun'
    start_urls = ['http://www.521609.com/daxuexiaohua/']
    #链接提取器：根据指定规则（allow,正则表达式）进行指定链接的提取
    link=LinkExtractor(allow=r'list[0-9]*\.html')
    #规则解析器，将连接提取器取到的链接进行指定规则（callback）的解析操作
    #follow=True 可以将链接提取器继续作用到链接提取器提取到的链接所对应的页面中
    #follow=False 只提取当前页链接
    rules = (Rule(link, callback='parse_item', follow=True),)
    def parse_item(self, response):
        print(response)
```


# 分布式爬虫
* 概念： 需要搭建一个分布式的机群，让其对一组资源进行分布联合爬取
* 作用： 提升爬取数据的效率
* 如何实现：
    * 安装scrapy-redis组件
    * 原生的scrapy是不可以实现分布式爬虫的，必须要让scrapy结合scrapy-redis进行
    * 为什么原生的scrapy不能实现分布式？
        * 调度器不可以被分布式机群共享
        * 管道不可以被分布式机群共享
    * scrapy-redis：
        * 可以给原生的scrapy框架提供可以被共享的管道和调度器
    * 实现流程
        * 创建一个工程
        * 创建一个基于Crawlspider的爬虫文件
        * 修改当前的爬虫文件
            * 导入：from scrapy_redis.spiders import RedisCrawlSpider
            * 将allowed_domain 和 start_url 注释掉
            * 添加一个属性：redis_key='pic' 可以被共享的调度器队列的名称
            * 编写数据解析相关操作
            ```python
            class SunSpider(RedisCrawlSpider):
                name = 'sun'
                redis_key='pic'
                rules = (Rule(LinkExtractor(allow=r'list[0-9]*\.html'), callback='parse_item', follow=True),)
            
                def parse_item(self, response):
                    li_list=response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
            for li in li_list:
                name=li.xpath('./a[2]/b/text()').extract_first()
                detail_url=li.xpath('./a[1]/@href').extract_first()
                item=SunproItem()
                item['name']=name
                item['detail_url'] = detail_url
                yield item
            ```
        * 修改配置文件：
            * 指定管道
            ```python
            ITEM_PIPELINES = {
              'scrapy_redis.pipelines.RedisPipeline': 400
            }
            ```
            * 指定调度器
            ```python
            # 使用scrapy-redis组件的去重队列
            DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
            # 使用scrapy-redis组件自己的调度器
            SCHEDULER = "scrapy_redis.scheduler.Scheduler"
            # 是否允许暂停
            SCHEDULER_PERSIST = True
            ```
            * 指定redis地址：
            ```python
            REDIS_HOST='127.0.0.1'
            REDIS_PORT=6379
            ```
        * redisx相关操作配置
             * 配置redis的配置文件：
                * linux mac:redis.conf
                * windows: redis.windows.conf
             * 打开修改配置文件
                * 将bind 127.0.0.1进行删除
                * 关闭保护模式：protected-mode yes改为no
             * 结合配置文件启动redis服务
                * redis-server 配置文件
             * 启动客户端
                * redis-cli
        * 执行工程：
            * scrapy runspider xxx.py
        * 向调度器队列中放入一个起始页url：
            * 调度器的队列在redis的客户端中
                * lpush pic www.xxx.com
        * 爬取到的数据存储在了redis的proName:item这个数据结构中