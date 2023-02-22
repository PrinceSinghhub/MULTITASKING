from threading import *
class mythread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        self.name=a
        print(f"Name: {self.name}")

# a=mythread("CODEX CODER")
# a.start()
class myclass(mythread):
    def __init__(self,a,b):
        # todo parent class thread call
        mythread.__init__(self, a)
        self.age=b
        print(f"age: {self.age}")



b=myclass("codex coder",19)
b.start()