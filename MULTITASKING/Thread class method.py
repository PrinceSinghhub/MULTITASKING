from threading import *
# todo using run() mrthod

class Mythread(Thread):
    # todo usinf run()mrthod
    print("using run() mrthod")
    def run(self):
        print("run() methode call")
t=Mythread()
t.start()
