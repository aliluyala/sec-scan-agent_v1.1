# -*- coding:utf-8 -*- 
#!/user/bin python
#Description: Description 
#Author:      Bing
#Email:       amzing_bing@outlook.com
#DateTime:    2017-01-11 22:38:34

import sys
sys.path.append("../../")

import gevent,time
from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()

from common.func import *
from core.frame import exploit
from core.database import redis_task

class Work(object):
	def __init__(self):
		self.pool = Pool(100)
		self.redis_task = redis_task
		self.poc_files = []
		self.exploit = []

	def run(self):
		while True:			
			if self.redis_task.scard("web_task") < 1 :
				time.sleep(2)
				print "no web task ..."
			else:
				try:
					for i in range(self.redis_task.scard("web_task")) :
						get_task = eval(self.redis_task.spop("web_task"))
					# get_task = {'model': 'subdomain', 'target': 'baidu.com', 'taskid': 'taskid-tsdf-1212'}
					model = str(get_task["model"])
					target = str(get_task["target"])
					taskid = str(get_task["taskid"])

					self.poc_files = get_web_poc(model)
					#执行poc
					if len(self.poc_files) > 0 :
						for poc_path in self.poc_files :
							poc_filename =  str(poc_path.split("/")[-1])
							#设置运行参数模板
							task = {"poc_path" : poc_path,"target" : target,"poc_filename" : poc_filename,"taskid" : taskid,"model" : model}
							#添加task任务到数组
							self.exploit.append(task)
						self.pool.map_async(exploit,self.exploit)
				except:
					pass

t = Work()
t.run()

#web
# task =  {'poc_path': 'C:\\Users\\Lagou\\Desktop\\sec-exp-scanner/models/web/web-subdomain-20170104-960730.py', 'model': 'subdomain', 'poc_filename': 'web-subdomain-20170104-960730.py', 'target': 'baifubao.com', 'taskid': 'taskid-tsdf-1212'}
# exploit(task)
