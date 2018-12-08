import re

filename = "py_dns_Server.py"
f = open(filename,'r')
f_tmp = open("py_dns_Server_tmp.py",'w+')

pattern = re.compile("^[0-9]{1,4}\\.")


while True:
    line_tmp = f.readline()
    if line_tmp:
        line_tmp = re.sub(pattern,"",line_tmp)
        f_tmp.write(line_tmp)
    else:break

f.close()
f_tmp.close()

#print re.sub(pattern,"","a4.335353ageet")


'''
reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
for ip in reip.findall(line):
print "ip>>>", ip
'''
