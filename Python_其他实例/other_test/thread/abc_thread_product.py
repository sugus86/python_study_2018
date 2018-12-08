#encoding=utf-8
import threading
import random
import time
from Queue import Queue

class Producer(threading.Thread):
    def __init__(self, threadname, queue):
        threading.Thread.__init__(self, name = threadname)
        self.sharedata = queue

    def run(self):
        for i in range(5):
            print self.getName(),'adding',i,'to queue'
            self.sharedata.put(i)
            time.sleep(random.randrange(10)/10.0)
        print self.getName(),'Finished'

# Consumer thread
class Consumer(threading.Thread):
    def __init__(self, threadname, queue):
        threading.Thread.__init__(self, name = threadname)
        self.sharedata = queue

    def run(self):
        for i in range(5):
            r = self.sharedata.get()
            print self.getName(),'got a value:',r
            time.sleep(random.randrange(10)/10.0)
        print self.getName(),'Finished'

def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    print 'Starting threads ...'
    producer.start()    
    consumer.start()
    producer.join()
    consumer.join()
    print 'All threads have terminated.'
if __name__ == '__main__':
    main()
