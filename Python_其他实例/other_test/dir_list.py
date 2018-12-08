
'''
import socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(('127.0.0.1', 1234))
'''

'''
import socket
solist=[x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
for x in solist:
    print x
'''

'''
import socket
solist=[x for x in dir(socket)]
solist.sort()
for x in solist:
    print x
'''

import logging
#list=[x for x in dir(logging) if 65<=ord(x[0])<=90]
list=[x for x in dir(logging) if x==x.upper()]
list.sort()
for x in list:
    print x
