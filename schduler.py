##A program for schduling

##import modules
import thread
import threading
import time

class Operation(threading._Timer):
    def __init__(self, *args, **kwargs):
        threading._Timer.__init__(self, *args, **kwargs)
        self.setDaemon(True)

    def run(self):
        while True:
            self.finished.clear()
            self.finished.wait(self.interval)
            if not self.finished.isSet():
                self.function(*self.args, **self.kwargs)
            else:
                return
            self.finished.set()

class Manager(object):

    ops = []

##add_operation function
    
    def add_operation(self, operation, interval, args=[], kwargs={}):
        op = Operation(interval, operation, args, kwargs)
        self.ops.append(op)
        thread.start_new_thread(op.run, ())

##stop function 
    def stop(self):
        for op in self.ops:
            op.cancel()
        self._event.set()

if __name__ == '__main__':
    
    # Print "Hello World!" every 5 seconds
        
    def hello():
        print "Hello World!"
##creating object for Manager class

    timer = Manager()
    
##calling add_operation function by Manager class object
    
    timer.add_operation(hello, 5)

    while True:
        time.sleep(.1)
