from threading import *
def pr():
    print(f"Child thread name: {current_thread().name}")
    # todo modify thread name
    current_thread().name = "Chlid Thread"
    print(f"Child thread Modify name: {current_thread().name}")

r=Thread(target=pr)
r.start()
print()
def display():
    print(f"Main thread name: {current_thread().name}")
    # todo modify thread name
    current_thread().name = "CODEX CODER Main Thread"
    print(f"Main thread Modify name: {current_thread().name}")
display()