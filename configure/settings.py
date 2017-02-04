#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-17 10:28:39
# Description:  coding 

import redis


#允许访问ip地址
allowip = ['127.0.0.1','x.x.x.1']

#**************************************************数据库配置项********************************************************************

redis_host = "127.0.0.1"
redis_passwd = ""
redis_port = 6379

redis_task_db = 6
redis_log_db = 7

redis_result_db = 8
