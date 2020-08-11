# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SunproPipeline:
    conn=None
    def open_spider(self,spider):
        self.conn=spider.conn
    def process_item(self, item, spider):
        dic={
            'name':item['name'],
            'detail':item['detail']
        }
        self.conn.lpush('totalData',dic)
        return item
