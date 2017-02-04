#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-17 13:54:37
# Description:  coding 

import sys
sys.path.append("../")

from configure.settings import *
from common.func import log_info,log_error

#**************************************************redis任务池连接信息********************************************************************

#web任务池
try:
    task_redis1 = redis.ConnectionPool(host = redis_host,port = redis_port,db = redis_task_db ,password = redis_passwd) 
    redis_task = redis.Redis(connection_pool = task_redis1)
except:
    log_error("[FALSE] redis task connect error ...")

#brute 任务池
try:
    task_redis3 = redis.ConnectionPool(host = redis_host,port = redis_port,db = redis_log_db ,password = redis_passwd) 
    redis_log = redis.Redis(connection_pool = task_redis3)
except:
    log_error("[FALSE] redis log connect error ...")

#result任务池
try:
    task_redis4 = redis.ConnectionPool(host = redis_host,port = redis_port,db = redis_result_db ,password = redis_passwd) 
    redis_result = redis.Redis(connection_pool = task_redis4)
except:
    log_error("[FALSE] redis rule connect error ...")
