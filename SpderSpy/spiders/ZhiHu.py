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
        cookie = 'q_c1=654622a1e9ee4223bbe92a46b7c9ab85|1505881411000|1505881411000; q_c1=3183d98881a74f36bc85712054ba5975|1505881411000|1505881411000; _zap=a128491a-ad09-4210-a4bb-5c8997c64394; l_cap_id="YjIxOTZmZTA5ZWNjNDhlZjkzMjgyMTY2YmI2MDUxZjg=|1506087510|482c129c5f8bca0dc784dc0411f859a404956836"; r_cap_id="MDYxNTMyYzBhZDljNDFjNjgxZmQ3OTBlOGI0ODEwYjU=|1506087510|f828475462a463d5ecee95912706684a25888f38"; cap_id="YTAxMTcwYTM3YzU1NDQzMDliYmQwOTlhY2YxZjI5NTQ=|1506087510|b6817f275a3ba10e16c6aab5537f810c7a831d20"; d_c0="AAACSAh7ZwyPTj_oyRq5ezrNOcR-k6-5tJs=|1505882895"; __utma=51854390.1102168530.1505882896.1506083558.1506087511.5; __utmz=51854390.1506087511.5.4.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20150905=1^3=entry_date=20170920=1; aliyungf_tc=AQAAAIAqnT8tAwkANwF0b/VR6ep+SlIa; _xsrf=11093c38-427f-43f3-8e7a-95a0f707a8ab; l_n_c=1; __utmc=51854390; capsion_ticket="2|1:0|10:1505914282|14:capsion_ticket|44:ZTdlMjE0MzcwMGQ1NGFjZjkzYTQyOWQ0MzBkMzZkZjA=|1a359008ff7e7b88cfa43bf5caa76fe56a07da383cdcd44d6a52d776939e8039"; __utmb=51854390.0.10.1506087511; z_c0="2|1:0|10:1506087591|4:z_c0|92:Mi4xNnJZUEFnQUFBQUFBQUFKSUNIdG5EQ2NBQUFDRUFsVk5wNV9zV1FDdTVSSFd6RnN4elNTeWRfWmZ3akpVT3BUakhR|4eec6f53266060ccfcc24ddd428c2f8df41ab6d4d006df1d7d728230614396c5"'
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
        