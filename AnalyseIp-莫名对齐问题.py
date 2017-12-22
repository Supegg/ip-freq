import re
import io
import datetime

"""
analyse ip change history
data eg:
2016-04-27 09:35:04,111.144.112.229
2016-04-26 17:30:31,111.144.112.229
"""

with open('loongson_ip_20171221.txt', 'r') as ips:
	line = ips.readline()
	last=re.split(',', line)
    print(line)
    last[0]=datetime.datetime.strptime(last[0], "%Y-%m-%d %H:%M:%S")

