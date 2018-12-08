import socket
import time, sys
from threading import Thread
from threading import Lock
from threading import Condition
import select
import logging

RCV_SIZE_DEFAULT = 32768
LISTEN_QUEUE_SIZE = 10
logging.basicConfig(level=logging.DEBUG)

class Controller(Thread):
    def __init__(self, host='172.31.130.30', port=6633):
        #Thread.__init__(self)
        self.active = True
        self.host = host
        self.port = port
        self.socs = []
        self.logger = logging.getLogger("controller")        

    def run(self):

        self.dbg_state = "starting"
        self.logger.info("Create/listen at " + self.host + ":" + 
                 str(self.port))
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, 
                                      socket.SO_REUSEADDR, 1)
        self.listen_socket.bind((self.host, self.port))
        self.dbg_state = "listening"
        self.listen_socket.listen(LISTEN_QUEUE_SIZE)
        self.logger.info("Waiting for switch connection")
        self.socs = [self.listen_socket]
        self.dbg_state = "running"
        self.switch_socket,self.switch_addr = self.listen_socket.accept()
        self.logger.info("Switch connected: %s", self.switch_addr)
        while self.active:
            try:
                sel_in, sel_out, sel_err = \
                    select.select(self.socs, [], self.socs, 1)
            except:
                print sys.exc_info()
                self.logger.error("Select error, disconnecting")
                self.disconnect()

            for s in sel_err:
                self.logger.error("Got socket error on: " + str(s) + ", disconnecting")
                self.disconnect()

            for s in sel_in:
                #if self._socket_ready_handle(s) == -1:
                    #self.disconnect()
                #client_s, _ = s.accept()
                data=self.switch_socket.recv(1024)
                #print data
                self.logger.info("Receive data : %s", data)

        self.dbg_state = "closing"
        self.logger.info("Exiting controller thread")
        self.shutdown()

    def shutdown(self):
        self.active = False
        try:
            self.switch_socket.shutdown(socket.SHUT_RDWR)
        except:
            self.logger.info("Ignoring switch soc shutdown error")
        self.switch_socket = None
        try:
            self.listen_socket.shutdown(socket.SHUT_RDWR)
        except:
            self.logger.info("Ignoring listen soc shutdown error")
        self.listen_socket = None
        '''
        with self.xid_cv:
            self.xid_cv.notifyAll()
        with self.connect_cv:
            self.connect_cv.notifyAll()
        '''
        self.dbg_state = "down"


    def disconnect(self, timeout=-1):
        if self.switch_socket:
            #self.socs.remove(self.switch_socket)
            self.switch_socket.close()
            self.switch_socket = None
            self.switch_addr = None
            #with self.connect_cv:
            #   self.connect_cv.notifyAll()
    
a = Controller()
a.run()



