from threading import *
def pr():
    print("This is a thread programe")
t=Thread(target=pr)
# todo call thread
t.start()