# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

class SpderspySpiderMiddleware(object):
 
    def process_request(self, request, spider):
         user_agent_random = random.choice(self.useragent)
         request.headers.setdefault('User-Agent', user_agent_random) #这样就是实现了User-Agent的随即变换
    useragent = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 ',
'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Opera/9.80 (Android 2.3.3; Linux; Opera Mobi/ADR-1111101157; U; es-ES) Presto/2.9.201 Version/11.50 ',
'Opera/9.80 (Android 3.2.1; Linux; Opera Tablet/ADR-1109081720; U; ja) Presto/2.8.149 Version/11.10',
'BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103 ',
' Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; FujitsuToshibaMobileCommun; IS12T; KDDI)',
'Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296; BlackBerry9800; U; AppleWebKit/23.370; U; en) Presto/2.5.25 Version/10.54 '
]
    

class RandomProxyMiddleware(object):

        def __init__(self,ip=''):  
            self.ip=ip  
            
        def process_request(self, request, spider):  
            IPPOOL=[  
            {"ipaddr":"61.129.70.131:8080"},  
            {"ipaddr":"61.152.81.193:9100"},  
            {"ipaddr":"120.204.85.29:3128"},  
            {"ipaddr":"219.228.126.86:8123"},  
            {"ipaddr":"61.152.81.193:9100"},  
            {"ipaddr":"218.82.33.225:53853"},  
            {"ipaddr":"223.167.190.17:42789"}]  
            thisip=random.choice(IPPOOL)  
            print("this is ip:"+thisip["ipaddr"])  
            request.meta["proxy"]="http://"+thisip["ipaddr"] 