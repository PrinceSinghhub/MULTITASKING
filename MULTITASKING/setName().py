from threading import *
def pr():
    print("This is a default child thread Name")
    # todo print thread name
    print(current_thread().getName())
    # todo change the deafult thread name
    current_thread().setName("Child Thread")
    print(f"modify thread name: {current_thread().getName()}")
t=Thread(target=pr)

t.start()

print()
def disp():
    print("This is a default Main thread Name")
    # todo print thread name
    print(current_thread().getName())
    # todo change the deafult thread name
    current_thread().setName("Main Thread")
    print(f"modify thread name: {current_thread().getName()}")
disp()