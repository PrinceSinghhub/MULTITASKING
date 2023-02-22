from threading import *
from time import *
arr = []
def collect():
    cm.acquire()
    for i in range(1,6):
        arr.append(i)
        sleep(1)
        print("Data collected...")
    cm.notify()
    cm.release()

def data():
    cm.acquire()
    cm.wait(timeout=1)
    cm.release()
    print(arr)

cm = Condition()
t1 = Thread(target=collect)
t2 = Thread(target=data)
t1.start()
t2.start()