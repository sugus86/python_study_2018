import hashlib
src = 'this is a md5 test.'.encode()
m = hashlib.md5()   
m.update(src)   
print(m.hexdigest())