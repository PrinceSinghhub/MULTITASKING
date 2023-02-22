from threading import*
from time import *
class company:
    def __init__(self):
        print("CODEX CODER COMPANY")
        print()
        self.lock=Lock()
        print(self.lock)

    def data(self,salary,post):
        print(f"Sallary: {salary}\nPost: {post}")
    def process(self,name,id,salary,post):
        self.lock.acquire(blocking=True,timeout=-1)
        print(self.lock)
        sleep(3)
        print(f"Employee Bio Data\nName: {name}\nCoustemer Id: {id}")
        current_thread().name=f"{name} Thread"
        print(f"Thread Name: {current_thread().name}")
        self.data(salary,post)
        self.lock.release()
        print()

r=company()
a1=Thread(target=r.process,args=("CODEX CODER","AX3006",157000,"CEO"))
a2=Thread(target=r.process,args=("CODEX","ZX300P",75000,"HR"))
a3=Thread(target=r.process,args=("CODER BABA","PO6004",160000,"GM"))
a1.start()
a2.start()
a3.start()
a1.join()
a2.join()
a3.join()
print("Thank You For Visiting My Company")