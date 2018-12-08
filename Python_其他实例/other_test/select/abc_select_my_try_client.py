#!/usr/bin/env python
import socket
host='172.31.130.30'
port=10000
s = [0] * 5
for i in range(5):
    s[i]=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s[i].connect((host,port))
    s[i].send('hello from client %d' %i)

import time
time.sleep(10)
for i in range(5):
    s[i].close()
