#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-17 10:36:40
# Description:  coding 
import sys
sys.path.append("../")

import imp,time,random

from common.func import *
from core.loger import c_loger

def exploit(task):
	taskid = str(task["taskid"])
	target = str(task["target"])
	model = str(task["model"])
	poc_path = str(task["poc_path"])

	poc_filename =  str(poc_path.split("/")[-1])
	try:
		exp_arg = str(task["exp_arg"]) 	
	except :
		exp_arg = ""

	try:
		username = str(task["username"])	
	except :
		username = ""

	try:
		password = str(task["password"])	
	except :
		password = ""

	try:
		#加载插件
		poc_class = imp.load_source('BingScan', poc_path)
		#初始化插件
		secscan = poc_class.BingScan(target= target,exp_args = exp_arg,username = username,password = password)
		#日志记录
		msg_info = 2
		c_loger(taskid = taskid ,target = target,exp_arg = exp_arg ,username = username ,password = password,msg_info = msg_info ,poc_filename = poc_filename ,model = model )
	except :
		msg_info = 3
		c_loger(taskid = taskid ,target = target ,exp_arg = exp_arg ,username = username ,password = password,msg_info = msg_info ,poc_filename = poc_filename ,model = model )

	try:
		#运行插件
		secscan.run()
		results = secscan.result
		if len(results) > 0 :
			msg_info = 1
			for result in results:
				#日志记录
				c_loger(taskid = taskid ,target = target ,exp_arg = exp_arg ,username = username ,password = password,msg_info = msg_info ,poc_filename = poc_filename ,model = model,result = result)
		else:
			pass
			#日志记录
			# msg_info = 0
			# c_loger(taskid = taskid ,target = target ,exp_arg = exp_arg ,username = username ,password = password,msg_info = msg_info ,poc_filename = poc_filename ,model = model)
	except:
		pass
		#日志记录
		# msg_info = 0
		# c_loger(taskid = taskid ,target = target ,exp_arg = exp_arg ,username = username ,password = password,msg_info = msg_info ,poc_filename = poc_filename ,model = model)

#web
# task =  {'poc_path': 'C:\\Users\\Lagou\\Desktop\\sec-exp-scanner/models/web/web-subdomain-20170104-960730.py', 'model': 'subdomain', 'poc_filename': 'web-subdomain-20170104-960730.py', 'target': 'baidu.com', 'taskid': 'taskid-tsdf-1212'}
# exploit(task)

#brute
# task = {'poc_path': 'C:\\Users\\Lagou\\Desktop\\sec-exp-scanner/models/brute/brute-subdomain-20170105-194849.py', 'model': 'subdomain', 'exp_arg': 'www', 'target': 'baifubao.com', 'taskid': 'taskid-tsdf-1212'}
# exploit(task)

#最后需要得到的结果
#result  = {'model': self.model, 'target': self.target, 'taskid': self.taskid, 'poc_path': self.poc_path,'exp_arg': exp_arg}
