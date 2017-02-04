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

from libraries.captcha import Captcha
from libraries.req import *

class BingScan(object):
    def __init__(self,  target = "",exp_args = "", username = "",password = ""):
        self.target = target
        self.result = []
        self.website = "https://www.threatcrowd.org"

    def run(self):
        if is_domain(self.target) == False :
            return []
        try:
            url = "{0}/searchApi/v2/domain/report/?domain={1}".format(self.website, self.target )
            content = http_request_get(url).content

            for sub in json.loads(content).get('subdomains'):
                if is_domain(sub):
                    self.result.append(sub.encode('gbk'))

            return list(set(self.result))
        except Exception as e:
            return 0

# netcraft = BingScan(target='aliyun.com')
# netcraft.run()
# print netcraft.result
