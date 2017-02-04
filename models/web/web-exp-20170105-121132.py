# -*- coding:utf-8 -*- 
#!/user/bin python
#Description: Description 
#Author:      Bing
#Email:       amzing_bing@outlook.com
#DateTime:    2017-01-14 21:04:00
import sys
sys.path.append("../../")

import re,os
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
			domain = self.target.split(".")[-2]+'.'+self.target.split(".")[-1]
			cmd_res = os.popen('nslookup -type=ns ' + domain).read()  # fetch DNS Server List
			dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
			if len(dns_servers) == 0:
				pass
			for singledns in dns_servers:
				cmd_res = os.popen('dig @%s axfr %s' % (singledns, domain)).read()

				if cmd_res.find('XFR size') > 0:
					self.result.append("dns_zone_tranfer_finder")
				else:
					pass
		except:
			pass

# netcraft = BingScan(target ='lagou.com')
# netcraft.run()
# print netcraft.result 

# domain = "baidu.com"
# cmd_res = os.popen('nslookup -type=ns ' + domain).read()  # fetch DNS Server List
# dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
# if len(dns_servers) == 0:
# 	pass
# for singledns in dns_servers:
# 	cmd_res = os.popen('dig @%s axfr %s' % (singledns, domain)).read()

# 	if cmd_res.find('XFR size') > 0:
# 		print ("dns_zone_tranfer_finder")
# 	else:
# 		pass

