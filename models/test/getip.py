# -*- coding:utf-8 -*- 
#!/user/bin python
#Description: Description 
#Author:      Bing
#Email:       amzing_bing@outlook.com
#DateTime:    2016-12-31 12:27:39

import pygeoip,os

res = os.getcwd().split("/utils")[0]

def get_geoip_code(address):
	geoip_path = str(res)+"/dict/collect/GeoLiteCity.dat"
	gi = pygeoip.GeoIP(geoip_path)
	add = gi.record_by_name(address)
	return (add["city"],add["country_name"])
	#gi.record_by_name

# print ({'country': get_geoip_code("106.38.73.242")})

import multiprocessing
import time

def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.start()
    print "p.pid:", p.pid
    print "p.name:", p.name
    print "p.is_alive:", p.is_alive()
