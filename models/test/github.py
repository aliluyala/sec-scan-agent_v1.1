#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../")
#from conf.globals import path
import time
import urllib
import requests
import datetime
import random
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
reload(sys)
sys.setdefaultencoding("utf-8")


session = requests.session()
header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'HTTPS':'1',
            'Referer':'https://github.com/',
            'Origin':'https://github.com',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Accept-Encoding':'gzip, deflate, br',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }

# get login token
csrfToken = pq(session.get('https://github.com/login', headers=header).text)('input[name="authenticity_token"]').val()
print csrfToken
# login
loginData = {'login':'', 'password':'', 'authenticity_token': csrfToken, 'utf8':'✓'} # 设置账号密码
res = session.post('https://github.com/session', data=loginData, headers=header)
print res.text

def submitMsg(keyword, projectTitle, projectUrl, fileTitle, fileUrl, code):
    #interface = 'http://0.0.0.0/dashboard/api/github-msg'  #** interface前端
   # fileUrl = urllib.unquote(fileUrl)
    data = {'keyword': keyword, 'projectTitle': projectTitle, 'projectUrl': projectUrl, 'fileTitle':fileTitle, 'fileUrl':fileUrl, 'code': code}
    #return requests.post(interface, data).text
    print data


def query(keyword):
    rs = []
    page = 1
    keywordTmp = urllib.quote(keyword)
    keywordTmp = keywordTmp.replace("%20", "+")
    while True:
        time.sleep(random.randint(1, 5))
        url = "https://github.com/search?p=%d&q=%s&ref=searchresults&type=Code&utf8=%s" % (page, keywordTmp, "%E2%9C%93")

        print url
        page = page+1
        code = session.get(url, headers=header).text
        soup = BeautifulSoup(code, "lxml")
        tmpList = soup.find_all(class_="code-list-item")

        noNext = code.find("<span class=\"next_page disabled\">Next</span>") > -1 or code.find("Next") == -1
	print noNext
        if noNext:
            print "####"+url

        for item in tmpList:
            site = "https://www.github.com"
            addr = item.find('p').find_all('a')
            projectUrl = site + addr[0].get('href')
            projectTitle = addr[0].text
            fileUrl = site + addr[1].get('href')
            fileTitle = addr[1].text
            code = str(item.find('table'))
            submitMsg(keyword, projectTitle, projectUrl, fileTitle, fileUrl, code)
        rs = rs + tmpList

        if noNext:
            break
    return rs

if __name__ == '__main__':
    items = ""
    all = []

    # 取远程服务器管理的关键词
    #keywords = requests.get("http://0.0.0.0/dashboard/api/search-keywords").json()  #**用于获取自定义的关键词
    keywords = [{"word":"@meili-inc.com"},]
    # 根据关键词检索代码
    for keyword in keywords:
        print keyword['word']
        rs = query(keyword['word'])
        if len(rs) > 0:
            print len(rs)
            all = all + rs
            print len(all)
    for item in all:
        items = items + str(item).replace("href=\"", "target=\"_blank\" href=\"https://www.github.com")


    code = '''
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="utf-8" />
            <title>信息搜集</title>
            <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
            <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-355fc5f5dc43030d495ea75b6bc8366695646a7566c13dd6ba2c2d358e1b5383.css" integrity="sha256-NV/F9dxDAw1JXqdba8g2ZpVkanVmwT3WuiwtNY4bU4M=" media="all" rel="stylesheet" />
            <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-7fae2d802a203f722465a757a5c1ecdb285d355fdcda038c10a2d20722dcf959.css" integrity="sha256-f64tgCogP3IkZadXpcHs2yhdNV/c2gOMEKLSByLc+Vk=" media="all" rel="stylesheet" />
            <script src="http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
            <script src="http://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
        </head>
        <body>
            <div class="code_search_results">
                <div class="code-list">
                    %s
                </div>
            </div
        </body>
        </html>
        ''' % items

    filename = "/Users/bing/%s.html" % datetime.datetime.now().strftime('%Y%m%d')  #** filename自定义路径
    writer = open(filename, 'w')
    writer.write(code)
    writer.close()



