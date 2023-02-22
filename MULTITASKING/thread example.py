from threading import *
def pr():
    pass
r=Thread(target=pr,name="Deafult Thread")
print(f"Deafult thread name: {r.name}")
r.name = "CODEX CODER THERAD"
print(f"Modify thread name: {r.name}")
