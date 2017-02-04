#coding:utf8
import sys,socket

#PortList = [21, 22, 23, 25, 80, 135, 137, 139, 443, 445, 1433, 1502, 3306, 3389, 8080, 9015,873,3128,8081,9080,1080,7001,110,9090,1521,1158,2100]
PortList = [80,8080,443]
#超时时间
Timeout = 2.0
#打开的端口列表
OpenPort = []


#获取C段IP函数
def getips(host):
		ip = []
		ip_pre = ""
		for pre in host.split('.')[0:3]:
			ip_pre = ip_pre + pre + '.'
		for i in range(1,49):
			l = (ip_pre+str(i))
			ip.append(l)		
		return ip
	
def Ping(ips):
	global Timeout,PortList,OpenPort
	for i in ips:
		for j in PortList:
			#address = (i,j)
			sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sk.settimeout(Timeout)
			try:
				sk.connect((i,j))
				print('Server %s port %d OK!' % (i,j))
			except Exception:
				pass
			sk.close()
			


Ping(getips('10.10.10.48'))






