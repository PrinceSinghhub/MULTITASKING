from threading import *
def stu_data():
    a = "CODEX CODER: CSE"
    b = "CODER: AI"
    c = "PRINCE SINGH: B TECH"
    print(f"{a}\n{b}\n{c}")

T = Thread(target=stu_data)


# todo check thread are daemon or not
print("before thread set",T.isDaemon())

# todo create a daemon thread
T.setDaemon(True)
print("After set thread",T.isDaemon())

# todo usining property thread are daemon or not
print("using property: ",T.daemon)
T.start()