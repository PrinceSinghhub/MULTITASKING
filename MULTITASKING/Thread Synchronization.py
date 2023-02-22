# todo Multitasking using Multiple Thread
# todo Two Threads acting on same method using Lock()
from threading import *
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = Lock()

    def reserve(self, need_seat):
        self.l.acquire(blocking=True)
        print('Available Seats:', self.available_seat)
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
        else:
            print('Sorry! All seats has alloted')
        self.l.release()

f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='CODEX CODER')
t2 = Thread(target=f.reserve, args=(1,), name='CODER')
t3 = Thread(target=f.reserve, args=(1,), name='CODER BABA')
t1.start()
t2.start()
t3.start()
# todo if we run then main thread bhi function me ja skta hai thats why using join()
t1.join()
t2.join()
t3.join()
print("Main Thread")