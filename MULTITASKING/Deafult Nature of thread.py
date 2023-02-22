from threading import *

def data():
    print("Main Thread")

    # todo create a child thread
    T2 = Thread(target=child)
    print("T2: ",T2.isDaemon())
    T2.start()

def child():
    print("Child thread create using T1")

# todo main thread if parent is non-daemon then child is also non-daemon
print("main thread if parent is non-daemon then child is also non-daemon")
mt = current_thread()
print(mt.getName())
print("MT:" ,mt.daemon)

# todo creat a child thread
T1 = Thread(target=data)
print("T1:",T1.isDaemon())

# todo if parent is daemon then child is also daemon
print("if parent is daemon then child is also daemon")
print("T1 Before:" ,T1.isDaemon())
T1.setDaemon(True)
print("T1 After:" ,T1.isDaemon())
T1.start()
T1.join()

