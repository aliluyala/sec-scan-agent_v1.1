import sys
sys.path.append("../../")

# from libraries.captcha import Captcha
from libraries.req import *
from splinter import Browser
import dns.resolver

class BingScan(object):
	def __init__(self,  target = "",exp_args = "", username = "",password = ""):
		if is_domain(target):
			self.target = target.split(".")[-2]+'.'+target.split(".")[-1]
			self.username = str(username)+"@"+str(self.target)
		else:
			return False
		self.password = password
		self.result = []

	def scanemail(self):
		browser = Browser("phantomjs")
		url = 'https://en.exmail.qq.com'
		try:
			browser.visit(url)
		except Exception as e:
			return
		#fill in username and password
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
		try:
			MX = dns.resolver.query(self.target,'MX')
			for result in MX:
				if "qq.com" in str(result.exchange):
					t = "ok"
				else:
					return []
			self.scanemail()
		except:
			pass


# t = BingScan(target="lagou.com",exp_args = '',username = "siyu.li",password = "tiandao123")
# t.run()
# print t.result


