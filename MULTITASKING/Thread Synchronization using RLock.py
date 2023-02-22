from threading import*
class company:
    def __init__(self):
        print("CODEX CODER COMPANY")
        print()
        # todo using RLock
        self.lock=RLock()
        print(self.lock)
        print()

    def data(self,salary,post):
        print(f"Sallary: {salary}\nPost: {post}")
    def process(self,name,id,salary,post):
        # todo locked multiple time
        self.lock.acquire()
        self.lock.acquire()
        self.lock.acquire()
        print(self.lock)
        print()
        print(f"Employee Bio Data\nName: {name}\nCoustemer Id: {id}")
        current_thread().name=f"{name} Thread"
        print(f"Thread Name: {current_thread().name}")
        self.data(salary,post)
        self.lock.release()
        self.lock.release()
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