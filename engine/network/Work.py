#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-17 19:06:06
# Description:  coding 


import sys
sys.path.append("../../")

import gevent
from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()

import socket,os,time
from common.func import *
from core.loger import net_loger
from core.database import redis_task

#**************************************************-获取端口和服务***********************************************************

def get_port_service(text):
	service_path = str(os.getcwd().split("sec-exp-scanner")[0])+"sec-exp-scanner/dictionary/nmap-services.txt"
	port_server = str(text)+"/tcp"
	with open(service_path,"r") as server:
		for finger in server.readlines():
			port = finger.strip().split(";")[1]
			if port == port_server:
				fingers = str(finger.strip().split(";")[0])
				return (port_server,fingers)
		return (port_server,"unknown")

#print get_port_service(6379)


class Work(object):
	def __init__(self, taskid="",target = ""):
		self.pool = Pool(200)
		self.target = target	#直接从数据库子域名结果读取目标
		self.taskid = taskid
		self.result = []
		self.timeout = 0.1

	def port_scan(self,port):
 		try:
			sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sd.settimeout(self.timeout)
			try:
				sd.connect((self.target,int(port)))
				self.result.append(get_port_service(port))
			except socket.error:
				pass	
			sd.close()
		except:
			pass

	def run(self):
		res = []
		for port in range(65535):
			res.append(port)
		self.pool.map(self.port_scan,res)


def service():
	while True:			
		if redis_task.scard("net_task") < 1 :
			time.sleep(2)
			print "no port task ..."
		else:
			try:
				for i in range(redis_task.scard("net_task")) :
					get_task = eval(redis_task.spop("net_task"))
				#get_task = {'model': 'net', 'target': 'baidu.com', 'taskid': 'taskid-tsdf-1212'}
				target = str(get_task["target"])
				if is_domain(target) or is_host(target):
					taskid = str(get_task["taskid"])
					t = Work(target=target,taskid=taskid)
					t.run()
					results = t.result
					msg_info = 1
					for result in results:
						net_loger(taskid = taskid ,target = target ,msg_info = msg_info ,result = result,model = "port")
			except:
				msg_info = 0
				net_loger(taskid = taskid ,target = target ,msg_info = msg_info,model = "port")



# t = Work(target="www.baidu.com",taskid="taskid-2323-23")
# t.run()
# print t.result
