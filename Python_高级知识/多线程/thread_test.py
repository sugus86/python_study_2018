import threading
class worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        pass
    def run(self):
        """thread worker function"""
        print('Worker')

t = worker()
t.start()
t.join()
