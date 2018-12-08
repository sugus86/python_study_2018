'''
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
'''


import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
    
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

#logging.basicConfig(level=logging.DEBUG)

#http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
