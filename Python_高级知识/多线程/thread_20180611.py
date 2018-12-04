import threading
import random,time

def random_time():
    return random.random()

def threadFunction(arg):
    for i in range(20):
        lock.acquire()
        #t=round(random_time(),3)
        t=2
        print('ThreadFuction - %d____%s____%d'%(arg,t,i))
        time.sleep(t)
        lock.release()
        
if __name__ == '__main__':
    lock = threading.Lock()
    threading.Thread(target = threadFunction, args=(1,)).start();
    threading.Thread(target = threadFunction, args=(2,)).start();
