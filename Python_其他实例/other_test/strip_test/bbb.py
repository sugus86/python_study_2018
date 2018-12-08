#!/usr/bin/python   
# -*- coding: utf-8 -*-   
import ftplib  
import os  
import socket  
  
HOST = 'ftp.mozilla.org'  
DIRN = 'pub/mozilla.org/webtools'  
FILE = 'bugzilla-4.5.6.tar.gz'  
def main():  
    try:  
        f = ftplib.FTP(HOST)  
    except (socket.error, socket.gaierror):  
        print 'ERROR:cannot reach " %s"' % HOST  
        return  
    print '***Connected to host "%s"' % HOST  
  
    try:  
        f.login()  
    except ftplib.error_perm:  
        print 'ERROR: cannot login anonymously'  
        f.quit()  
        return  
    print '*** Logged in as "anonymously"'  
    try:  
        f.cwd(DIRN)  
    except ftplib.error_perm:  
        print 'ERRORL cannot CD to "%s"' % DIRN  
        f.quit()  
        return  
    print '*** Changed to "%s" folder' % DIRN  
    try:  
        #传一个回调函数给retrbinary() 它在每接收一个二进制数据时都会被调用   
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)  
    except ftplib.error_perm:  
        print 'ERROR: cannot read file "%s"' % FILE  
        os.unlink(FILE)  
    else:  
        print '*** Downloaded "%s" to CWD' % FILE  
    f.quit()  
    return  
  
if __name__ == '__main__':  
    main() 
