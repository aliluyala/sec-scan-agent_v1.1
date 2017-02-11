import sys
sys.path.append("../../")

# from libraries.captcha import Captcha
from libraries.req import *
from splinter import Browser
import dns.resolver

class BingScan(object):
	def __init__(self,  target = "",exp_args = "", username = "",password = ""):
		if is_domain(target):
			if target.split(".")[-1] == "cn":
				self.target = target.split(".")[-3]+'.'+target.split(".")[-2]+'.'+'cn'
				self.username = str(username)+"@"+str(self.target)
			else:
				self.target = target.split(".")[-2]+'.'+target.split(".")[-1]
				self.username = str(username)+"@"+str(self.target)
		else:
			return False
		self.password = password
		self.result = []

	def scanemail(self):
		# print self.target,self.username,self.password
		browser = Browser("phantomjs")
		url = 'https://en.exmail.qq.com'
		try:
			browser.visit(url)
		except Exception as e:
			return

		browser.find_by_id('inputuin').fill(self.username)
		browser.find_by_id('pp').fill(self.password)
		#click the button of login
		browser.find_by_id('btlogin').click()
		#time.sleep(1)
		redictUrl = 'https://en.exmail.qq.com/cgi-bin/frame_html'
		redictUrl2 = 'http://en.exmail.qq.com/cgi-bin/readtemplate'
		# print self.username,self.password
		# print  browser.url
		if redictUrl2 in browser.url or redictUrl in browser.url:
			out = (self.username,self.password)
			browser.quit()
			self.result.append(out)
		else:
			#print "[N]:%s : %s login failed" %(username,password)
			browser.quit()

	def run(self):
		self.scanemail()
		# try:
			# MX = dns.resolver.query(self.target,'MX')
			# for result in MX:
			# 	if "qq.com" in str(result.exchange):
			# 		t = "ok"
			# 	else:
			# 		return []

			#self.scanemail()
		# except:
		# 	pass


# t = BingScan(target="vipkid.com.cn",exp_args = '',username = "siyu.li",password = "tiandao123")
# t.run()
# print t.result


