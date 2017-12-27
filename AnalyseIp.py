import re
import io
import datetime

"""
analyse ip change history

date:2017-12-27
note:  
    fix last ip's last-time=0 bug
    format output string  

date:2017-12-22
note:creat&analyse first

data eg:
2016-04-27 09:35:04,111.144.112.229
2016-04-26 17:30:31,111.144.112.229
"""

history = []
cur = []
cnt = 0
dt = 0
min=100000000
max=0
with open('loongson_ip_20171221.txt', 'r') as ips:
    d1 = datetime.datetime.now()
    for line in ips:
        cnt+=1
        cur = re.split(',', line.strip())
        cur[0] = datetime.datetime.strptime(cur[0], "%Y-%m-%d %H:%M:%S")

        if not history:#add first ip
            history.append(cur)
            #print(cur)
        else:
            if cur[1] != history[-1][1]:
                history.append(cur)
                dt = cur[0] - history[-2][0]
                dt = round(dt.days*24 + dt.seconds / 3600, 2)
                if dt<min:
                    min=dt
                if dt>max:
                    max=dt
                history[-2].append(dt)
                print('%s  %s\t%s'%(history[-2][0].strftime('%Y-%m-%d %H:%M:%S'),history[-2][1].ljust(15),history[-2][2]))
    
    #calc last ip's last-time
    dt = datetime.datetime.now()-history[-2][0]
    dt = dt.days*24 + round(dt.seconds / 3600, 2)
    history[-1].append(dt)
    print('%s  %s\t%s'%(history[-1][0].strftime('%Y-%m-%d %H:%M:%S'),history[-1][1].ljust(15),history[-1][2]))

    #calc run time
    dt = datetime.datetime.now() - d1
    dt = dt.seconds + dt.microseconds / 1000000

print('\nsummary')
print("\tbegin:\t\t %s"%d1.strftime("%H:%M:%S"))
print("\tend:\t\t %s"%datetime.datetime.now().strftime("%H:%M:%S"))
print("\trun time:\t %.1f s" %dt)
print("\trecord num:\t %d" %(cnt))
print("\trecord time:\t %d days" %((history[-1][0]-history[0][0]).days))
print("\trecord ips:\t %d times" %len(history))
print("\tmin:\t\t %d hour" %min)
print("\tmax:\t\t %d hours" %max)

#print format: http://www.runoob.com/w3cnote/python3-print-func-b.html