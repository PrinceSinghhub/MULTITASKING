from threading import *
from time import *
class myclass:
    def family(self,a):
        self.detail=a
        print(f"{self.detail} DETAILS")
        sleep(2)
        self.papa(),self.mami(),self.sister(),self.me()
    def papa(self):
        print(f"Father Name: Baliram Singh")
        sleep(2)
    def mami(self):
        print(f"Mother Name: Ansu Devi")
        sleep(2)
    def sister(self):
        print(f"Sister Name: Anushka Singh")
        sleep(2)
    def me(self):
        print(f"My Name: Codex Coder")
        sleep(2)
r=myclass()
t=Thread(target=r.family,args=("FAMILLY",))
t.start()