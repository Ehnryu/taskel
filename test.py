from taskel import Tasks
import time
tm = Tasks()
def myfunc():
  print("hello world")

t = tm.create(target=myfunc,daemon=False)
t.start()
time.sleep(2)

