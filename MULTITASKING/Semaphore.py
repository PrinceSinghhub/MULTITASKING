from threading import*
class student:
    def __init__(self,ID):
        a="WellCome CODEX CODER COLLAGE"
        print(a.center(155))
        self.ID=ID
        # todo using Semaphore 2 is a thread
        self.lock=Semaphore(2)
        print(f"Thread Nmae: {self.lock}")
        print()
    def student_data(self,name,branch,fee):
        self.lock.acquire()
        print(f"Avalible of No pf Thread for calling: {self.lock._value}")
        print(f"Student Name: {name}\nStudent ID: {self.ID}\nStudent Branch: {branch}\nStudent Fee: {fee}")
        self.lock.release()
        # todo kitni baar bhi relese kr skti hai es method me
        # self.lock.release()
        # self.lock.release()
        # self.lock.release()

        print()
x=student(101)
a1=Thread(target=x.student_data,args=("CODEX CODER","CSE",65000))
x.ID=102
a2=Thread(target=x.student_data,args=("CODEX","IT",75000))
x.ID=103
a3=Thread(target=x.student_data,args=("CODER BABA","AI",160000))
a1.start()
a2.start()
a3.start()