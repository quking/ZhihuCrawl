# encoding:utf-8

import sys
from scrapy.spiders import CrawlSpider
import scrapy
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from SpderSpy.items import SpderspyItem

reload(sys)
sys.setdefaultencoding('utf8')

class ZH(CrawlSpider):
    name = 'zhihu'
    allowed_domains = ['https://www.zhihu.com/']
    def start_requests(self):
        coo = {}
        cookie = 'your cookie'  #你自己的cookie
        for seg in cookie.split(';'):
            key,value = seg.split('=',1)
            coo[key] = value
        return [scrapy.FormRequest('https://www.zhihu.com/question/26049726',cookies=coo,callback=self.parse)]
    def parse(self, response):
        print "spider beginning"
        words = open('clould.txt','w+')
        url = response.url
        driver = webdriver.PhantomJS()
        driver.get(url)
        clk = driver.find_elements_by_xpath('//button[text()="查看更多回答"]')
        count = 0
        while clk:
            for i in clk:
                i.click()
                time.sleep(3)
            clk = driver.find_elements_by_xpath('//button[text()="查看更多回答"]')
        item = SpderspyItem()
        soup = BeautifulSoup(driver.page_source,'html.parser',from_encoding='utf-8')
        item['content'] = soup.find_all('span',class_="RichText CopyrightRichText-richText")
        for i in item['content']:
            print unicode.encode(i.get_text(),'utf-8')
            words.write(unicode.encode(i.get_text(),'utf-8'))
            count = count+1
        print '总共有：%d 条评论'%count
        driver.quit()
        
