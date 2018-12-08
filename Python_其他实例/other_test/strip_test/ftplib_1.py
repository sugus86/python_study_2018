01.#!/usr/bin/python   
02.# -*- coding: utf-8 -*-   
03.import ftplib  
04.import os  
05.import socket  
06.  
07.HOST = 'ftp.mozilla.org'  
08.DIRN = 'pub/mozilla.org/webtools'  
09.FILE = 'bugzilla-3.6.7.tar.gz'  
10.def main():  
11.    try:  
12.        f = ftplib.FTP(HOST)  
13.    except (socket.error, socket.gaierror):  
14.        print 'ERROR:cannot reach " %s"' % HOST  
15.        return  
16.    print '***Connected to host "%s"' % HOST  
17.  
18.    try:  
19.        f.login()  
20.    except ftplib.error_perm:  
21.        print 'ERROR: cannot login anonymously'  
22.        f.quit()  
23.        return  
24.    print '*** Logged in as "anonymously"'  
25.    try:  
26.        f.cwd(DIRN)  
27.    except ftplib.error_perm:  
28.        print 'ERRORL cannot CD to "%s"' % DIRN  
29.        f.quit()  
30.        return  
31.    print '*** Changed to "%s" folder' % DIRN  
32.    try:  
33.        #传一个回调函数给retrbinary() 它在每接收一个二进制数据时都会被调用   
34.        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)  
35.    except ftplib.error_perm:  
36.        print 'ERROR: cannot read file "%s"' % FILE  
37.        os.unlink(FILE)  
38.    else:  
39.        print '*** Downloaded "%s" to CWD' % FILE  
40.    f.quit()  
41.    return  
42.  
43.if __name__ == '__main__':  
44.    main() 