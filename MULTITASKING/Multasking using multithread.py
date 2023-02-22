from threading import *
class myclass:
    def __init__(self,a):
        self.n=a
        print(f"{self.n} Member")
    def papa(self,a):
        print(f"Father Name: {a}")
    def mami(self,b):
        print(f"Mother Name: {b}")
    def sister(self,c):
        print(f"Sister Name: {c}")
    def me(self,d):
        print(f"My Name: {d}")

r=myclass("Head")
t1=Thread(target=r.papa,args=("Baliram Singh",))
t1.start()
r1=myclass("Co-Head")
t2=Thread(target=r1.mami,args=("Ansu Devi",))
t2.start()
r2=myclass("Junier Child")
t3=Thread(target=r2.sister,args=("Anushka Singh",))
t3.start()
r3=myclass("Sinear Child")
t4=Thread(target=r3.me,args=("Codex Coder",))
t4.start()
