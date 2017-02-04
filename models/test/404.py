#!/usr/bin/env python 
import sys,re,requests
#from lib.consle_width import getTerminalSize
import dns.resolver,re

my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8''114''114.114.114.144','208.67.222.222','180.76.76.76','199.91.73.222','216.146.35.35','8.26.56.26','156.154.70.1','199.85.126.10','112.124.47.27','42.120.21.30','223.5.5.5','123.125.81.6','218.30.118.6','203.156.201.157','211.139.163.6','211.136.28.228','202.96.128.86','202.96.199.132','202.96.0.133','202.102.227.68','210.21.4.130','211.95.1.97']

_stat200 = []
_stat403 = []
_stat_q =[]
result = []

f = open(sys.argv[1],"r")
for i in f.readlines():
    result.append(i.strip())

sets = {}.fromkeys(result).keys()


for i in sets:
	try:
		reg = r'https'
		if re.findall(reg,i):
			answers = my_resolver.query(str(i.strip()[8:]))
			ip = ', '.join([answer.address for answer in answers])
		else:                
			answers = my_resolver.query(str(i.strip()[7:]))
			ip = ', '.join([answer.address for answer in answers])
		url = i.strip()
		try:
			r = requests.get(url,timeout=5)
			if str(r.status_code) == str(200):
				_stat200.append((str(r.status_code),url,str(r.headers['server']),str(r.headers['X-Powered-By']),str(ip)))
			elif str(r.status_code) == str(403):
				_stat403.append((str(r.status_code),url,str(r.headers['server']),str(r.headers['X-Powered-By']),str(ip)))
			else:
				_stat_q.append((str(r.status_code),url,str(r.headers['server']),str(r.headers['X-Powered-By']),str(ip)))
			#print str(r.status_code),url,str(r.headers['server']),str(r.headers['X-Powered-By']),str(ip)
		except:
			pass
	except:
		pass

print "################Status results########################"

for i in _stat200:
    print i[0],i[1],i[2],i[3],i[4]
print "------------------------------------------------------"
for i in _stat403:
    print i[0],i[1],i[2],i[3],i[4]
print "------------------------------------------------------"
for i in _stat_q:
    print i[0],i[1],i[2],i[3],i[4]








