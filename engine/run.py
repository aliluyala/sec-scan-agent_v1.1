#!/user/bin python
# -*- coding:utf-8 -*- 
# Author:Bing
# Contact:amazing_bing@outlook.com
# DateTime: 2017-01-18 11:11:31
# Description:  coding 

import sys
sys.path.append("../")

import multiprocessing
from engine.network.Work import service
from engine.web.Work import Work as web
from engine.brute.Work import Work as brute

def web_laucher():
	webs = web()
	webs.run()

def brure_laucher():
	brutes = brute()
	brutes.run()

if __name__ == "__main__":
	p1 = multiprocessing.Process(target = web_laucher)
	p2 = multiprocessing.Process(target = service)
	p3 = multiprocessing.Process(target = brure_laucher)

	p1.start()
	p2.start()
	p3.start()

