from threading import*
class mythread:
    def pr(self,a,b): print("addition is:",a+b)

class myclass(mythread):
    print("hello my class")
r=myclass()
t=Thread(target=r.pr,args=(10,20))
t.run()