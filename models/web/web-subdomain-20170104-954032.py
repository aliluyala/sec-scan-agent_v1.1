#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2016-12-21 11:46:49
# Description:  coding 
import sys
sys.path.append("../../")

from libraries.captcha import Captcha
from libraries.req import *

class BingScan(object):
    def __init__(self,  target = "",exp_args = "", username = "",password = ""):
        self.target = target
        self.result = []
        self.url = 'http://i.links.cn/subdomain/'

    def run(self):
        if is_domain(self.target) == False :
            return []
        try:
            payload = {
                'b2': 1,
                'b3': 1,
                'b4': 1,
                'domain': self.target 
            }
            r = http_request_post(self.url,payload=payload).text
            subs = re.compile(r'(?<=value\=\"http://).*?(?=\"><input)')
            for item in subs.findall(r):
                if is_domain(item):
                    self.result.append(item.encode('gbk'))

            return list(set(self.result))
        except Exception as e:
            return 0

# netcraft = BingScan(target ='baifubao.com')
# netcraft.run()
# print netcraft.result
