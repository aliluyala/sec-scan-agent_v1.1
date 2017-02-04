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

    def run(self):
        if is_domain(self.target) == False :
            return []
        try:
            self.fetch_chinaz()
            self.fetch_alexa_cn()
            return list(set(self.result))
        except Exception as e:
            return 0

    def fetch_chinaz(self):
        url = 'http://alexa.chinaz.com/?domain={0}'.format(self.target )
        r = http_request_get(url).content
        subs = re.compile(r'(?<="\>\r\n<li>).*?(?=</li>)')
        result = subs.findall(r)
        for sub in result:
            if is_domain(sub):
                self.result.append(sub)

    def fetch_alexa_cn(self):
        sign = self.get_sign_alexa_cn()
        if sign is None:
            raise Exception("sign_fetch_is_failed")
        else:
            (domain,sig,keyt) = sign

        pre_domain = self.target .split('.')[0]

        url = 'http://www.alexa.cn/api_150710.php'
        payload = {
            'url': domain,
            'sig': sig,
            'keyt': keyt,
            }
        r = http_request_post(url, payload=payload).text

        for sub in r.split('*')[-1:][0].split('__'):
            if sub.split(':')[0:1][0] == 'OTHER':
                break
            else:
                sub_name = sub.split(':')[0:1][0]
                sub_name = ''.join((sub_name.split(pre_domain)[0], domain))
                if is_domain(sub_name):
                    self.result.append(sub_name)

    def get_sign_alexa_cn(self):
        url = 'http://www.alexa.cn/index.php?url={0}'.format(self.target )
        r = http_request_get(url).text
        sign = re.compile(r'(?<=showHint\(\').*?(?=\'\);)').findall(r)
        if len(sign) >= 1:
            return sign[0].split(',')
        else:
            return None

# netcraft = BingScan(target ='lagou.com')
# netcraft.run()
# print netcraft.result
