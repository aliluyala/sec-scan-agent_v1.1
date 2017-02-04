#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-17 16:44:03
# Description:  coding 

import sys
sys.path.append("../../")

from core.database import redis_task
from common.func import *

class TaskCenter(object):
	def __init__(self, taskid="",target = "",model=""):
		self.target = target
		self.taskid = taskid
		self.model = str(model)

	def web(self):
		task = {"taskid": self.taskid ,"target": self.target,"model":self.model}
		try:
			redis_task.sadd("web_task",task)
			#记录日志
			info = "web taskid: %s ,target: %s model: %s is start " % (self.taskid,self.target,self.model)
			log_info(info)
		except :
			info = "web taskid: %s ,target: %s model: %s is start false" % (self.taskid,self.target,self.model)
			log_error(info)

	def net(self):
		task = {"taskid": self.taskid ,"target": self.target,"model":self.model}
		try:
			redis_task.sadd("net_task",task)
			#记录日志
			info = "net taskid: %s ,target: %s model: %s is start " % (self.taskid,self.target,self.model)
			log_info(info)
		except :
			info = "net taskid: %s ,target: %s model: %s is start false" % (self.taskid,self.target,self.model)
			log_error(info)

	def brute(self):
		task = {"taskid": self.taskid ,"target": self.target,"model":self.model}
		try:
			redis_task.sadd("brute_task",task)
			#记录日志
			info = "brute taskid: %s ,target: %s  model: %s is start " % (self.taskid,self.target,self.model)
			log_info(info)
		except :
			info = "brute taskid: %s ,target: %s model: %s is start false" % (self.taskid,self.target,self.model)
			log_error(info)

	def run(self):
		if is_domain(self.target) or is_host(self.target):
			self.web()
			self.net()
			self.brute()
		else:
			log_error("target format error .... re enter , please ")



t  = TaskCenter(taskid="taskid-tsdf-1212",target="lagou.com",model="subdomain")
t.run()
