from urllib import request as urllib2

data = {'apikey': 'abcde12345','url': 'http://www.sina.com'}
requesturl = 'http://api.htm2pdf.co.uk/urltopdf?apikey={apikey}&url={url}'.format(**data)
print("Convert baidu.com to pdf")
result = urllib2.urlopen(requesturl)
localFile = open('mypdf.pdf', 'w')
localFile.write(result.read().decode())
localFile.close()

'''
#字节对象b
b = b"example"
#字符串对象s
s = "example"
print(b)
print("example")

#将字符串转换为字节对象
b2 = bytes(s,encoding='utf8')  #必须制定编码格式
# print(b2)
#字符串encode将获得一个bytes对象
b3 = str.encode(s)
b4 = s.encode()
print(b3)
print(type(b3))
print(b4)
#将字节对象decode将获得一个str对象
s2 = bytes.decode(b)
s3 = b.decode()
print(s2)
print(s3)
'''


''' 
data = {'apikey': 'abcde12345','url': 'http://www.baidu.com'}
requesturl = 'http://api.htm2pdf.co.uk/urltopdf?apikey={apikey}&url={url}&top=0&bottom=0&left=0&right=0'.format(**data)
result = urllib2.urlopen(requesturl)
localFile = open('mypdf.pdf', 'w')
localFile.write(result.read())
localFile.close()
'''



'''
http://api.htm2pdf.co.uk/urltopdf?apikey=abcde12345&url=http://blog.csdn.net/cupidove/article/details/23121859
'''
