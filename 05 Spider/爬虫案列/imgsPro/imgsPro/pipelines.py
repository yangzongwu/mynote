# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


#class ImgsproPipeline:
#    def process_item(self, item, spider):
#        return item
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