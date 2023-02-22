from threading import *
class mythread(Thread):
    print("this is a child class of thread class")
a=mythread()
print(a.name)