# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiproPipeline:
    # 用来处理item类型对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收一个item就被调用一次
    fp=None
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp=open('scrapyPro/爬虫案列/qiubaiPro/qiubai.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author=item['author']
        content=item['content']
        self.fp.write(author+':'+content)
        return item#就会传递给下一个即将执行的管道类

    def close_spider(self,spider):
        print("结束")
        self.fp.close()

# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
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