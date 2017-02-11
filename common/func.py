# -*- coding:utf-8 -*- 
#!/user/bin python
#Description: Description 
#Author:      Bing
#Email:       amzing_bing@outlook.com
#DateTime:    2017-01-11 20:36:22

import re,logging,random
import os


#**************************************************设置基础路径********************************************************************


BASE_DIR = os.getcwd().split("sec-scan-agent")[0]

# #日志文件目录
# LOG_PATH = BASE_DIR  +" sec-exp-scanner/log/"  

#POC插件总目录
POC_PATH = BASE_DIR+"sec-scan-agent/models/"

#字典目录
DICT_PATH = BASE_DIR+"sec-scan-agent/dictionary/"

#**************************************************-判断目标工具***********************************************************

#判断是否为域名
def is_domain(domain):
    domain_regex = re.compile(
        r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z', re.IGNORECASE)
    return True if domain_regex.match(domain) else False

#判断是否为ip
def is_host(host):
    ip_regex = re.compile(r'(^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])$)', re.IGNORECASE)
    return True if ip_regex.match(host) else False

#**************************************************-日志记录工具***********************************************************

logger = logging.getLogger("Bing-Robot")
logger.setLevel(logging.DEBUG)

#log_file = logging.FileHandler(str(LOG_PATH+'%s.log' % date2))
log_terminal = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#log_file.setFormatter(formatter)
log_terminal.setFormatter(formatter)

#logger.addHandler(log_file)
logger.addHandler(log_terminal)

def log_info(msg):
    logger.info(msg)

def log_error(msg):
    logger.error(msg)

#**************************************************遍历所有POC文件********************************************************************

#默认查找全部py文件
def fuzzyfinder(user_input, pocs_path):
        pocs_path = POC_PATH+str(pocs_path)
        suggestions = []
        files = os.listdir(pocs_path)
        #pattern = '^(domain_).*?'+user_input+'.*?\.py$'  
        pattern = '.*?'+user_input+'.*?\.py$'
        regex = re.compile(pattern) 
        for item in files:
            match = regex.search(item) 
            if match and item != '__init__.py':
                suggestions.append((len(match.group()), match.start(), pocs_path+'/'+item))
        return [x for _, _, x in sorted(suggestions)]

#获取web插件
def get_web_poc(user_search=""):
	#poc = fuzzyfinder(user_search, pocs_path)
	poc = fuzzyfinder(user_search,"web")
	return poc


#获取brute插件
def get_brute_poc(user_search=""):
	#poc = fuzzyfinder(user_search, pocs_path)
	poc = fuzzyfinder(user_search,"brute")
	return poc

# print get_web_poc('')
# print get_brute_poc('')

#**************************************************遍历所有字典文件********************************************************************

def fuzzyfinder_dict(user_input, pocs_path):
        dict_path = DICT_PATH+str(pocs_path)
        suggestions = []
        files = os.listdir(dict_path)
        #pattern = '^(domain_).*?'+user_input+'.*?\.py$'  
        pattern = '.*?'+user_input+'.*?\.txt$'
        regex = re.compile(pattern) 
        for item in files:
            match = regex.search(item) 
            if match and item != '__init__.py':
                suggestions.append((len(match.group()), match.start(), dict_path+'/'+item))
        return [x for _, _, x in sorted(suggestions)]

#获取brute字典
def get_brute_dict(user_search=""):
    #poc = fuzzyfinder(user_search, pocs_path)
    poc = fuzzyfinder_dict(user_search,"")
    poc = poc[0]
    #poc = "".join(poc)
    return poc

# print fuzzyfinder_dict("mail-username-mxing", "")
# print get_brute_dict("mail")


#**************************************************随机任务id***********************************************************

def TaskHashId():
    times = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    result = "TASKID-"+str(times)
    return result

def ModelHashId(sub):
    times = time.strftime("-%Y%m%d-", time.localtime())
    salt = []
    for i in range(0,6):
        salt.append(str(random.randint(0,9)))
        salts = "".join(salt)
    result = str(sub)+str(times)+str(salts)
    return result

def PocHashId():
    times = time.strftime("%Y%m%d-", time.localtime())
    salt = []
    for i in range(0,6):
        salt.append(str(random.randint(0,9)))
        salts = "".join(salt)
    result = "SEC-"+str(times)+str(salts)
    return result
