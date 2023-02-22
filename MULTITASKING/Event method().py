from threading import *
import time

def walk():

    time.sleep(1)
    x.set()

    print("GREEN LIGHT")

    time.sleep(5)
    print("RED LIGHT ON")
    x.clear()

def command():

    x.wait()

    while x.is_set():

        print("YOU CAN GO ...........")
        time.sleep(0.5)

    print("Sorry......red signal stop now")


x = Event()
a=Thread(target=walk)
b=Thread(target=command)
a.start()
b.start()