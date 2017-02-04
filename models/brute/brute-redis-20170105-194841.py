#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-18 12:01:37
# Description:  coding 
import sys
sys.path.append("../../")

from libraries.captcha import Captcha
from libraries.req import *
import requests,socket

class BingScan(object):
	def __init__(self,  target = "",exp_args = "", username = "",password = ""):
		self.target = target
		self.username = username
		self.password = password
		self.port = 6379
		self.result = []

	def run(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((self.target,int(self.port)))
			s.send("INFO\r\n")
			result = s.recv(1024)
			if "redis_version" in result:
			 	self.result.append("unauthorized")
			else:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((self.target,int(self.port)))
				s.send("AUTH %s\r\n"%(self.password))
				result = s.recv(1024)
				if '+OK' in result:
					self.result.append(self.password)
		except Exception,e:
			pass

# t = BingScan(target="10d",username = "",password = "1234qwer~")
# t.run()
# print t.result
