from threading import *
from queue import *
from time import *

class Producer:
    def __init__(self):
        self.q = Queue()

    def insert_data(self):
        for i in range(1,6):
            print("data collected",i)
            self.q.put(i)
            sleep(1)

class consumer:
    def __init__(self,obj):
        self.object = obj

    def exces_data(self):
        for i in range(1,6):
            print("Excess data: ", self.object.q.get(i))

p = Producer()
c = consumer(p)

t1 = Thread(target=p.insert_data)
t2 = Thread(target=c.exces_data)
t1.start()
t2.start()

