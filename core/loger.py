#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-17 11:26:25
# Description:  coding 

import sys
sys.path.append("../")

from common.func import *
from core.database import redis_log,redis_result

def spider_loger(taskid = '' ,target = '' ,result = '' ,msg_info = 0 ,exp_arg = '' ,username = '' ,password = '' ,poc_filename = '' ,model = '' ):
	pass

def web_loger(taskid = '' ,target = '' ,result = '' ,msg_info = 0 ,exp_arg = '' ,username = '' ,password = '' ,poc_filename = '' ,model = '' ):
	msg_info = int(msg_info)
	if msg_info == 0:
		result_info = {"taskid" : taskid , "target" : target , "poc" : poc_filename , "msg_info" : msg_info ,"model" : model }
		# log_error(result_info)
		redis_result.sadd("{0}_result_error".format(model),result_info)
	elif msg_info == 1:
		result_info = {"taskid" : taskid , "target" : target ,"msg_info" : msg_info ,"model" : model ,"result" : result}
		log_info(result_info)
		redis_result.sadd("{0}_result_ok".format(model),result_info)
	elif msg_info == 2:
		result_info = {"taskid" : taskid , "target" : target , "poc" : poc_filename , "msg_info" : msg_info ,"model" : model }
		log_info(result_info)
		redis_log.sadd("{0}_loading_ok".format(model),result_info)
	elif msg_info == 3:
		result_info = {"taskid" : taskid , "target" : target , "poc" : poc_filename , "msg_info" : msg_info ,"model" : model }
		# log_error(result_info)
		redis_log.sadd("{0}_loading_ok".format(model),result_info)
	else:
		pass

def net_loger(taskid = '' ,target = '' ,result = '' ,msg_info = 0 ,exp_arg = '' ,username = '' ,password = '' ,poc_filename = '' ,model = '' ):
	result_info = {"taskid" : taskid , "target" : target ,"msg_info" : msg_info ,"result" : result}
	log_info(result_info)
	redis_result.sadd("{0}_result_ok".format(model),result_info)

def brute_loger(taskid = '' ,target = '' ,result = '' ,msg_info = 0 ,exp_arg = '' ,username = '' ,password = '' ,poc_filename = '' ,model = '' ):
	msg_info = int(msg_info)
	if msg_info == 0:
		result_info = {"taskid" : taskid , "target" : target , "poc" : poc_filename , "msg_info" : msg_info ,"model" : model,"exp_arg" : exp_arg,"username" : username ,"password" : password }
		# log_error(result_info)
		redis_result.sadd("{0}_result_error".format(model),result_info)
	elif msg_info == 1:
		result_info = {"taskid" : taskid , "target" : target ,"msg_info" : msg_info ,"model" : model ,"result" : result}
		log_info(result_info)
		redis_result.sadd("{0}_result_ok".format(model),result_info)
	elif msg_info == 2:
		result_info = {"taskid" : taskid , "target" : target , "poc" : poc_filename , "msg_info" : msg_info ,"model" : model,"exp_arg" : exp_arg,"username" : username ,"password" : password  }
		# log_info(result_info)
		redis_log.sadd("{0}_loading_ok".format(model),result_info)
	elif msg_info == 3:
		result_info = {"taskid" : taskid , "target" : target , "poc" : poc_filename , "msg_info" : msg_info ,"model" : model,"exp_arg" : exp_arg,"username" : username ,"password" : password  }
		# log_error(result_info)
		redis_log.sadd("{0}_loading_error".format(model),result_info)
	else:
		pass

def rule_loger(taskid = '' ,target = '' ,result = '' ,msg_info = 0 ,exp_arg = '' ,username = '' ,password = '' ,poc_filename = '' ,model = '' ):
	pass

def c_loger(taskid = '' ,target = '' ,result = '' ,msg_info = 0 ,exp_arg = '' ,username = '' ,password = '' ,poc_filename = '' ,model = '' ):
	poc_filename = str(poc_filename)
	if poc_filename.startswith("spider",0,7):
		print "spider"
		#spider_loger(taskid = taskid ,target = target ,result = result ,msg_info = msg_info ,exp_arg = exp_arg ,username = username ,password = password ,poc_filename = poc_filename ,model = model )
	elif poc_filename.startswith("web",0,3):
		web_loger(taskid = taskid ,target = target ,result = result ,msg_info = msg_info ,exp_arg = exp_arg ,username = username ,password = password ,poc_filename = poc_filename ,model = model )
	elif poc_filename.startswith("brute",0,7):
		brute_loger(taskid = taskid ,target = target ,result = result ,msg_info = msg_info ,exp_arg = exp_arg ,username = username ,password = password ,poc_filename = poc_filename ,model = model )
	elif poc_filename.startswith("rule",0,5):
		print "rule"
		#rule_loger(taskid = taskid ,target = target ,result = result ,msg_info = msg_info ,exp_arg = exp_arg ,username = username ,password = password ,poc_filename = poc_filename ,model = model )
	pass

