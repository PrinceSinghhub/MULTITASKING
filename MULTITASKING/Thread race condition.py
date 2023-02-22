from threading import *
class hiearing:
    def __init__(self,seat,start,finish):
        self.seat=seat
        self.start=start
        self.finish=finish
    def process(self,name,coding_rank):
        print("Employe Details")
        if self.seat>0:
            if (coding_rank >= self.start and coding_rank <= self.finish):
                print(f"Congrechulation your are selected: {name}\nYour Coding_rank is: {coding_rank}")
                print(f"Running Thread Name: {current_thread().name}")
                self.seat -= 1
            else:
                print(f"Excepted DATA only: {self.start} to {self.finish}")
                print(f"Sorry Your Coding_rank is not setisfied our data : {name}\nYour Coding_rank is: {coding_rank}")
                print(f"Running Thread Name: {current_thread().name}")
        else:
            print(f"Sorry Set are not avalible: {name}")


r=hiearing(2,1,10)
t=Thread(target=r.process,name="Thread of Codex Coder",args=("Codex Coder",8))
t1=Thread(target=r.process,name="Thread of CODER",args=("CODER",1))
t2=Thread(target=r.process,name="Thread of CODER BABA",args=("CODER BABA",1))
t.start()
t1.start()
t2.start()