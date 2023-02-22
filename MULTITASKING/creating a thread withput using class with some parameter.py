from threading import *
def pr(a,b):
    x=a+b
    y=a*b
    z=a-b
    print(f"Using Thread\nadd: {x} multi: {y} sub: {z}")
r=Thread(target=pr,args=(10,20))
r.start()
