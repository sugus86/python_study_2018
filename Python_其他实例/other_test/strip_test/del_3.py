fh = open('aaa.py')
fh_tmp = open('bbb.py','w+')
#for line in fh.readlines():
for line in fh:
    if line:
        #fh_tmp.write(line)
        #fh_tmp.write("user_add")
        fh_tmp.write(line[3:])

fh.close()
fh_tmp.close()
        
