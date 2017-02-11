# sec-scan-agent
this is agent in Python,use distributed design

#### Usage

Install dependent packages or modules：

```
pip install splinter,redis,gevent,requests
brew install phantomjs,dig
```
configure settings file,as follow :

```
allowip = ['127.0.0.1','x.x.x.1']

#**************************************************database options********************************************************************
redis_host = "127.0.0.1"
redis_passwd = ""
redis_port = 6379

redis_task_db = 6
redis_log_db = 7

redis_result_db = 8

```
if you changed dir name,please modify "common/func.py" file content,as follow:
```
BASE_DIR = os.getcwd().split("sec-scan-agent")[0]

#POC插件总目录
POC_PATH = BASE_DIR+"sec-scan-agent/models/"

#字典目录
DICT_PATH = BASE_DIR+"sec-scan-agent/dictionary/"
```

excute command,as follow:
```
#this is add task 
python task.py 
#this is run engine
python engine/run.py

```


Poc dependency file:
```
from libraries.captcha import Captcha
from libraries.req import http_request_post,http_request_get
from libraries.common import *
```

#### bug
The version has  some bugs,please waiting for upgrade.

#### issue
if you have some good ideas or some sugguest, Welcome to leave a message for me or discuss😁







