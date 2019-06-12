# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import urllib.request
import random

class Dbtop250Pipeline(object):
    def process_item(self, item, spider):
        mysql = pymysql.connect('localhost', 'root', '100521', 'python')
        imgurl = 'E:/PyCharm 2018.2.4/pycode/touch/dbtop250/image/' + str(random.randint(10000, 99999)) + '.jpg'
        urllib.request.urlretrieve(url=item['image'][0], filename=imgurl)
        sql = "insert into doubantop250 (title,content,director,image,alltime) values ('" + str(item['title'][0]) + "','" + str(
            item['content'][0]) + "','" + str(item['director'][0]) + "','"+ str(imgurl) + "','" + str(item['time'][0]) + "');"
        res = mysql.query(sql)
        if res:
            print('数据写入成功')
        #关闭数据库
        mysql.close()
        return item
