# sec-scan-agent
this is agent in Python,use distributed design

#### Usage

安装需要的依赖包或模块：
```
from splinter import Browser
install phantomjs,dig
```
poc提供的依赖文件:
```
http_request_post(url, payload, body_content_workflow=False, allow_redirects=allow_redirects, custom_cookie="")

from libraries.captcha import Captcha
from libraries.req import *
from libraries.common import *
```

bug:

poc的字典和参数需要从libraries创建；如一些密码，子域名，目录等；建立一个依赖库文件，从数据库获取信息进行组合；方便poc调用;
如：
在libraries文件夹下定义一个文件；用来回去数据库各项爆破的字典配置，mysql用户密码，邮箱用户和密码，redis密码等；
把全部获取到的配置，存放到一个变量里面(如：mysql_pwd = "select username,password from dict")；然后poc直接调用;如:
from libraries import mysql_pwd
print mysql_pwd  
可直接调用!


待后期改进代码，没时间写...


