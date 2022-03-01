
import time
import taskel
tm = taskel.Tasks()
def myfunc():
  print("hello world")

t = tm.create(target=myfunc,daemon=False)
t.loop(sec=5)
time.sleep(14)
print("all_tasks: " + str(tm.tasklist))
t.stop()
