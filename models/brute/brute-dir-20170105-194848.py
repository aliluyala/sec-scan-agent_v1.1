# -*- coding:utf-8 -*- 
#!/user/bin python
#Description: output system information
#Author:      Bing
#Email:       amzing_bing@outlook.com
#DateTime:    2016-12-15 21:52:57

import sys
sys.path.append("../../")

from libraries.captcha import Captcha
from libraries.req import *
import requests

class BingScan(object):
	def __init__(self,  target = "",exp_args = "", username = "",password = ""):
		self.target = target
		self.exp_args = exp_args
		self.result = []

	def dir_check(self,url):
		#return requests.get(url, stream=True, headers=headers, timeout=timeout, proxies=proxies, allow_redirects=allow_redirects)
		return http_request_get(url)

	def run(self):
		if is_domain(self.target) == False :
			return []
 		
		url = "http://"+self.target+"/"
		url2 = "https://"+self.target+"/"
		try:
 			results = self.dir_check(url)
 			results2 = self.dir_check(url2)
			if results.status_code == requests.codes.ok:
				url = url+str(self.exp_args)
				# print url
 				dir_exists = self.dir_check(url)
 				#print type(dir_exists.status_code),dir_exists.status_code
 				status = str(dir_exists.status_code) 
 				if status in ['301', '302',"200","403"]:
 					self.result.append((url,status))
 			elif results2.status_code == requests.codes.ok:
				url2 = url2+str(self.exp_args)
				# print url2
 				dir_exists = self.dir_check(url2)
 				status = str(dir_exists.status_code) 
 				if status in ['301', '302',"200","403"]:
 					self.result.append((url,status))	
		except:
			pass


# t = BingScan(target="www.lagou.com",exp_args = '.bash_history',username = "",password = "")
# t.run()
# print t.result

