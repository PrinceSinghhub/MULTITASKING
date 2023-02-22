from threading import *
def pr():
    for i in range(5):
        print(f"Video publish by Child Thread: {i}")
r = Thread(target=pr)
r.start()
for i in range(5):
    print(f"Video publish by Main Thread: {i}")
