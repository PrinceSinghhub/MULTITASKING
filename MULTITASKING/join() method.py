from threading import *
# todo using join() mrthod
class jointhread(Thread):
    # todo usinf run()mrthod
    print("using join() mrthod")
    def run(self):
        for i in range(5):
            print("child thread call")
t=jointhread()
t.start()
# todo using join() mrthod
t.join()
for i in range(5):
    print("main thread call")