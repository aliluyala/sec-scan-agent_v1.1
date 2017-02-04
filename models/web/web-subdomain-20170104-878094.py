#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2016-12-21 11:46:49
# Description:  coding 
import sys
sys.path.append("../../")

import requests
req = requests.Session()

from libraries.captcha import Captcha
from libraries.req import *

class BingScan(object):
    def __init__(self,  target = "",exp_args = "", username = "",password = ""):
        self.target = target
        self.result = []
        self.url = 'http://api.chaxun.la/toolsAPI/getDomain/'
        self.verify = ""

    def run(self):
        if is_domain(self.target) == False :
            return []
        try:
            timestemp = time.time()
            url = "{0}?0.{1}&callback=&k={2}&page=1&order=default&sort=desc&action=moreson&_={3}&verify={4}".format(
                self.url, timestemp, self.target , timestemp, self.verify)
            result = json.loads(req.get(url).content)
            if result.get('status') == '1':
                for item in result.get('data'):
                    if is_domain(item.get('domain')):
                        self.result.append(item.get('domain').encode('gbk'))
            elif result.get('status') == 3:
                pass
            return list(set(self.result))
        except Exception as e:
            return 0

    def download(self, url):
        try:
            r = req.get(url)
            with open("captcha.gif", "wb") as image:     
                image.write(r.content)
            return True
        except Exception, e:
            return False

    def verify_code(self):
        timestemp = time.time()
        imgurl = 'http://api.chaxun.la/api/seccode/?0.{0}'.format(timestemp)
        if self.download(imgurl):
            captcha = Captcha()
            code_result = captcha.verification(filename='captcha.gif')
            self.verify = code_result.get('Result')

# netcraft = BingScan(target ='lagou.com')
# netcraft.run()
# print netcraft.result
