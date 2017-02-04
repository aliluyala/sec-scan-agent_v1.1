# -*- coding:utf-8 -*- 
#!/user/bin python
#Description: output system information
#Author:      Bing
#Email:       amzing_bing@outlook.com
#DateTime:    2016-12-15 21:52:57

import sys
sys.path.append("../../")
from conf.globals import path
import nmap,sys
import pygeoip


def get_geoip_code(address):
	geoip_path = str(path)+"/dict/port/GeoLiteCity.dat"
	gi = pygeoip.GeoIP(geoip_path)
	add = gi.record_by_name(address)
	return add["city"],add["country_name"]

class Lnmap:
	"""
	host,hostname,port,server,system
	"""
	def __init__(self):
		self.arg = []

	def run(self,host):
		nm=nmap.PortScanner()
		nm.scan(hosts=host,arguments='-O')
		try:
			address = get_geoip_code(ip)
		except:
			address = "lnternat"
		for ip in nm.all_hosts():
			item_results = {}
			if nm[ip]['status']['state'] != 'up':
				continue
			else:
				item_results['ip'] = ip
				try:
					portlist = nm[ip]['tcp'].keys()
				except:
					portlist = []
				#print portlist
				#print nm[ip]['osmatch'][0]['name']
				if len(portlist) > 0:
					item_results['open'] = []
					for port in portlist:
						if nm[ip]['tcp'][port]['state'] != 'closed':
							print 'ip:',ip,'port:',port,'service:',nm[ip]['tcp'][port]['name'],'systeminfo:',nm[ip]['osmatch'][0]['name'],"location:",address
							#nm[ip].hostname()

				
#Lnmap().run(str(sys.argv[1]))
#print  get_geoip_code("www.qq.com")














'''
import pygeoip

def get_geoip_code(address):
    gi = pygeoip.GeoIP('/usr/share/GeoIP/GeoIP.dat')
    return gi.country_code_by_addr(address)

result.updte({'country': get_geoip_code(nmap_host.address)})


[
{'osclass': [{'osfamily': 'OS X', 'vendor': 'Apple', 'cpe': ['cpe:/o:apple:os_x:10.10'], 'type': 'general purpose', 'osgen': '10.10.X', 'accuracy': '100'}, 
{'osfamily': 'OS X', 'vendor': 'Apple', 'cpe': ['cpe:/o:apple:os_x:10.11'], 'type': 'general purpose', 'osgen': '10.11.X', 'accuracy': '100'}], 'line': '6894', 'name': 'Apple OS X 10.10 (Yosemite) - 10.11 (El Capitan) (Darwin 14.0.0 - 15.4.0)', 'accuracy': '100'}
]
'''


