[![support](https://baikal.io/badges/x)](https://baikal.io/x) [![License](https://img.shields.io/:license-gpl3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/Canbing007/sec-portscan-agent)
[![python](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/c38266fc482844e5b5d451583b1a04e9/badge.svg)](https://www.quantifiedcode.com/app/project/c38266fc482844e5b5d451583b1a04e9)

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







