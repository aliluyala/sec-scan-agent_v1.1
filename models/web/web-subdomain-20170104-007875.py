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
        self.timeout = 0.5
        self.site = 'http://searchdns.netcraft.com'

    def run(self):
        if is_domain(self.target) == False :
            return []
        try:
            self.cookie = self.get_cookie().get('cookie')
            url = '{0}/?restriction=site+contains&position=limited&host=.{1}'.format(
                self.site, self.target )
            r = http_request_get(url, custom_cookie=self.cookie)
            self.parser(r.text)
            return list(set(self.result))
        except Exception, e:
            return 0

    def parser(self, response):
        npage = re.search('<A href="(.*?)"><b>Next page</b></a>', response)
        if npage:
            for item in self.get_subdomains(response):
                if is_domain(item):
                    self.result.append(item.encode('gbk'))
            nurl = '{0}{1}'.format(self.site, npage.group(1))
            r = http_request_get(nurl, custom_cookie=self.cookie)
            time.sleep(3)
            self.parser(r.text)
        else:
            for item in self.get_subdomains(response):
                if is_domain(item):
                    self.result.append(item.encode('gbk'))

    def get_subdomains(self, response):
        _regex = re.compile(r'(?<=<a href\="http://).*?(?=/" rel\="nofollow")')
        domains = _regex.findall(response)
        for sub in domains:
            yield sub

    def get_cookie(self):
        try:
            cmdline = 'phantomjs ph_cookie.js'
            run_proc = subprocess.Popen(cmdline,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            (stdoutput,erroutput) = run_proc.communicate()
            response = {
                'cookie': stdoutput.rstrip(),
                'error': erroutput.rstrip(),
            }
            return response
        except Exception, e:
            return {'cookie':'', 'error': str(e)}

# netcraft = BingScan(target ='aliyun.com')
# netcraft.run()
# print netcraft.result 

