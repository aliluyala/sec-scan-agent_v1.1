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
from random import Random,uniform
from urllib import quote

def random_sleep():
    time.sleep(uniform(0,2))

def random_str(randomlength=8):
    rstr = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        rstr += chars[random.randint(0, length)]
    return rstr.lower()

class BingScan(object):
    def __init__(self,  target = "",exp_args = "", username = "",password = ""):
        self.target = target
        self.result = []
        self.token = ""
        self.subjects = []
        self.hashs = []
        self.num_result = 0
        self.website = 'https://www.google.com/transparencyreport/jsonp/ct'

    def run(self):
        if is_domain(self.target) == False :
            return []
        self.parser_subject()
        self.hashs = list(set(self.hashs)) # unique sort hash
        self.parser_dnsname()
        self.result = list(set(self.result))
        #self.subjects = list(set(self.subjects))
        return self.result

    def parser_subject(self):
        try:
            callback = random_str()
            url = '{0}/search?domain={1}&incl_exp=true&incl_sub=true&token={2}&c={3}'.format(
                    self.website, self.target , quote(self.token), callback)
            content = http_request_get(url).content
            result = json.loads(content[27:-3])
            self.token = result.get('nextPageToken')
            for subject in result.get('results'):
                if subject.get('subject'):
                    self.result.append(subject.get('subject').encode("gbk"))
                if subject.get('hash'):
                    self.hashs.append(subject.get('hash').encode("gbk"))
        except Exception as e:
            pass

        if self.token:
            self.parser_subject()

    def parser_dnsname(self):
        for hashstr in self.hashs:
            try:
                callback = random_str()
                url = '{0}/cert?hash={1}&c={2}'.format(
                        self.website, quote(hashstr), callback)
                content = http_request_get(url).content
                result = json.loads(content[27:-3])
                if result.get('result').get('subject'):
                    self.subjects.append(result.get('result').get('subject').encode("gbk"))
                if result.get('result').get('dnsNames'):
                    self.result.extend(result.get('result').get('dnsNames').encode("gbk"))
            except Exception as e:
                pass
            random_sleep()

# netcraft = BingScan(target='lagou.com')
# netcraft.run()
# print netcraft.result
