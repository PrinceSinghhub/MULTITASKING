# when non demon thread is terminate then demon thread also terminate automitacily

from threading import *
from time import sleep

def teacher():
    for i in range(1,11):
        print("class: ",i)
        sleep(0.9)

t = Thread(target=teacher)
t.setDaemon(True)
t.start()

sleep(5)
print("Class finished (non daemon thread)",current_thread().name)
