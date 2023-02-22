from threading import *
def pr():
    print("This is a child thread")
    # todo print thread name object
    print(current_thread())
t=Thread(target=pr)
t.start()
print()
print("This is a Main thread")
# todo print thread name object
print(current_thread())