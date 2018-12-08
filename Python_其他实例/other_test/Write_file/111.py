f = open("idel_27.txt",'r')
f_tmp = open('tmp_27.txt','w')
lines  = f.readlines()	
for line in lines:
	if not line[:-1].strip():
		continue
	line_split = line.split(":")
	#print line_split
	if "Port Current Power" == line_split[0].strip():
		print line_split[1][:-1]
		f_tmp.write(line_split[1])

f.close()
f_tmp.close()
