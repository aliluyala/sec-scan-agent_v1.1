#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-09 10:33:46
# Description:  coding 
import sys
sys.path.append("../../")

import gevent
from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()

from common.func import get_brute_dict

"""
一种是所有任务，一种是选择模块任务

"""
class Brute(object):
	def __init__(self, taskid = "",target = "",model = "",poc_path = ""):
		self.pool = Pool(100)
		self.model = model
		self.taskid = taskid
		self.target = target
		self.poc_path = poc_path
		self.task = []

	#读取测试列表
	def dict_exp(self,dict_poc):
		result = []
		with open("{0}".format(dict_poc),'r')  as f :
			for exp in f :
				result.append(str(exp.strip()))
		return {}.fromkeys(result).keys()


	#邮箱1--名+姓组合的密码
	def mark_password(self):
		result = []
		text = ["123","1234","!@#"]
		mxing = self.dict_exp(get_brute_dict("mail-username-mxing"))
		for user in mxing:
			for pwd in text:
				result.append((user,str(user+pwd)))
		return {}.fromkeys(result).keys()

	#邮箱2--域名组合的密码
	def mail_pwd(self):
		result = []
		text = ["123","2016","!@#"]
		mxing = self.dict_exp(get_brute_dict("mail-username-mxing"))
		target = str(self.target.split(".")[-2].lower())
		for user in mxing:
			for pwd in text:
				result.append((user,str(target+pwd)))
		return {}.fromkeys(result).keys()

	#邮箱3--全部组合
	def mail_pwd_dict(self):
		result = self.mark_password()
		result.extend(self.mail_pwd())
		return {}.fromkeys(result).keys()

	#端口服务--组合密码
	def service_pwd(self):
		result = []
		pwd_dict = ['123456','admin','root','password','123123','123','{user}','{user}{user}','{user}1','{user}123','{user}@123','{user}2016','{user}2015','{user}2014','{user}!','{user}1234','','P@ssw0rd!!','qwa123','12345678','test','123qwe!@#','123456789','123321','1314520','666666','000000','1234567890','8888888','qwerty','1qaz2wsx','abc123','abc123456','1q2w3e4r','123qwe','p@ssw0rd','p@55w0rd','password!','p@ssw0rd!','password1','r00t','tomcat','apache','system'," ","1234qwer~"]
		user =  str(self.target.split(".")[-2].lower())
		for pass_ in pwd_dict:
			pass_ = str(pass_.replace('{user}', user))
			result.append(pass_)
		return {}.fromkeys(result).keys()

	#端口服务--组合密码
	def service_pwd_dict(self):
		result = []
		user_dict = ["root","admin","sa","ftp","administrator","cisco","postgres","tomcat"," "]
		pwd_dict = ['123456','admin','root','password','123123','123','{user}','{user}{user}','{user}1','{user}123','{user}@123','{user}2016','{user}2015','{user}2014','{user}!','{user}1234','','P@ssw0rd!!','qwa123','12345678','test','123qwe!@#','123456789','123321','1314520','666666','000000','1234567890','8888888','qwerty','1qaz2wsx','abc123','abc123456','1q2w3e4r','123qwe','p@ssw0rd','p@55w0rd','password!','p@ssw0rd!','password1','r00t','tomcat','apache','system'," ","1234qwer~"]
		for user in user_dict:
			for pass_ in pwd_dict:
				pass_ = str(pass_.replace('{user}', user))
				result.append((user,pass_))
		return {}.fromkeys(result).keys()

	def dict_poc(self,model = "subdo"):
		result = self.dict_exp(get_brute_dict(model))	#根据模块选择的字典(xss,list,subdomain,mail)
		return  {}.fromkeys(result).keys()

	#file文件格式替换--组合
	def file_dict(self,filetype="json"):
		result = []
		web_dir = self.dict_poc("dir")
		for user in web_dir:
			pass_ = str(user.replace('{user}', filetype))
			result.append(pass_)
		return {}.fromkeys(result).keys()

	def brute_first(self,exp_arg):
		exp_arg = {'model': self.model, 'target': self.target, 'taskid': self.taskid, 'poc_path': self.poc_path,'exp_arg': exp_arg}
		self.task.append(exp_arg)


	def brute_second(self,exp_arg):
		test = ""
		if type(exp_arg) == type(test):
			exp_arg = ("",exp_arg)
		exp_arg = {'model': self.model, 'target': self.target, 'taskid': self.taskid, 'poc_path': self.poc_path,'username': exp_arg[0],'password':exp_arg[1]}
		self.task.append(exp_arg)


	def run(self):
		web_subdomain = self.dict_poc("subdomain")
		web_dir = self.file_dict()
		web_mail = self.mail_pwd_dict()

		redis_pwd = self.service_pwd()
		net_pwd = self.service_pwd_dict()
		poc_filename =  str(self.poc_path.split("/")[-1])
		# print web_subdomain,web_list
		# print web_mail,net_pwd
		# print web_subdomain

		if self.model == "":
			if "subdomain" in poc_filename:
				self.pool.map(self.brute_first,web_subdomain)

			if "dir" in poc_filename:
				self.pool.map(self.brute_first,web_dir)

			if "mail" in poc_filename:
				pass
			else:
				pass

		else:
			if "subdomain" in poc_filename:
				self.pool.map(self.brute_first,web_subdomain)

			elif "dir" in poc_filename:
				self.pool.map(self.brute_first,web_dir)

			elif "mail" in poc_filename:
				self.pool.map(self.brute_second,web_mail)

			elif "redis" in poc_filename:
				self.pool.map(self.brute_second,redis_pwd)
			else:
				pass



	
# t = Brute(taskid="1212",target="tiandaoedu.com",poc_path="C:\\Users\\Lagou\\Desktop\\sec-exp-scanner/models/brute/brute-redis-20170105-194841.py",model ="redis") 
# t.run()
# print len(t.task)
# for i in t.task:
# 	print i




#['C:\\Users\\Lagou\\Desktop\\sec-exp-scanner/models/brute/brute-dir-20170105-194848.py', 'C:\\Users\\Lagou\\Desktop\\sec-exp-scanner/models/brute/brute-mail-20170109-922525.py', 'C:\\Users\\Lagou\\Desktop\\sec-exp-scanner/models/brute/brute-subdomain-20170105-194849.py']

# t = Brute(taskid="1212",target="baidu.com",poc_path="web-subdomain-sd.py",model ="mail")  #2个参数
# #print t.mark_password()
# print t.service_pwd_dict()

# t = Brute(taskid="1212",target="baidu.com",poc_path="web-subdomain-sd.py",model ="subdomain")  #2个参数
# print t.mark_password()


# try:
# 	self.dict_poc = self.dict_exp(get_brute_dict(self.model))	#根据模块选择的字典
# except:
# 	self.dict_poc = ""

# #邮箱用户
# try:
# 	self.dict_user = self.dict_exp(get_brute_dict("mail-user"))
# except:
# 	self.dict_user = ""
