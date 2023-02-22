from threading import *
def pr():
    print("This is a default child thread Name")
    # todo print thread name
    print(current_thread().getName())
t=Thread(target=pr)
t1=Thread(target=pr)
t.start()
t1.start()
print()
print("This is a default Main thread Name")
# todo print thread name
print(current_thread().getName())