# -*- coding:utf-8 -*- 
#!/user/bin python
#Description: Description 
#Author:      Bing
#Email:       amzing_bing@outlook.com
#DateTime:    2017-01-14 17:05:46

import sys
sys.path.append("../../")

# from libraries.captcha import Captcha
from libraries.req import *
import dns.resolver


class BingScan(object):
	def __init__(self,  target = "",exp_args = "", username = "",password = ""):
		self.target = target
		self.exp_args = exp_args
		self.result = []

	def domain(self,test):
		try:
			dns_server = ["114.114.114.114","114.114.115.115","180.76.76.76","223.5.5.5","223.6.6.6","8.8.8.8"]
			my_resolver = dns.resolver.Resolver()
			my_resolver.nameservers = ["114.114.114.114","114.114.115.115","180.76.76.76","223.5.5.5","223.6.6.6","8.8.8.8"]
			target = str(test)
			answers = my_resolver.query(target)
			ips = ', '.join([answer.address for answer in answers])
			return (ips,target)
		except:
			return ''

	def run(self):
		if is_domain(self.target) == False :
			return []
		try:
			target = str(self.exp_args)+'.'+str(self.target)
			result = self.domain(target)
			if result == "":
				pass
			else:
				self.result.append(target)
		except:
			pass


# netcraft = BingScan(target ='aliyun.com',exp_args = 'wwsdfw')
# netcraft.run()
# print netcraft.result 

