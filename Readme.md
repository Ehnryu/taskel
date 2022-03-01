# Taskel
The python library for all types of tasks

### Installation:
`pip install taskel`

### Quick Start:
```python
from taskel import Tasks
import time
tm = Tasks()
def myfunc():
  print("hello world")

t = tm.create(target=myfunc,daemon=False)
t.loop(sec=5)
time.sleep(14)
print("all_tasks: " + str(tm.tasklist))
t.stop()
```


### Usage
(not an example)
```python
from taskel import Tasks
tm = Tasks()
def myfunc(hi,bye):
  print("hello world")
def myfunctwo(hi):
  print(f"ran me only once {hi}")
t = tm.create(target=myfunc,args=["hi","bye"],daemon=False)
t.loop(sec=20)
print("you can go about your buisness/program")
print("with slightly beautiful aesthetic interruptions")
print("interruptions like hello world every 20 seconds")
print("however this is not all...")
print("you can just start tasks normally too")
ttwo = tm.create(target=myfunctwo,args=["well hello there"])
ttwo.start()
print("yet with all these interuptions, wouldn't you want to name your tasks?")
x = tm.create(target=myfunctwo,args=["i'm named yay :)"],name="X")
all_tasks = tm.tasklist
print(all_tasks)
print("while you can do: `t.stop()`")
print("to remove it from the tasklist:")
tm.end(x)
print("check if a task is running?")
t.running
print("normal stop ends the task after the round is complete if it is in the middle of one")
print("to force stop a task:")
tm.end(ttwo,force=True)
print("or `ttwo.force('stop')`")
print("for daemon, change the value to true")
print("eg:")
print('t = tm.create(target=myfunc,args=["hi","bye"],daemon=True)')
print("use daemon for background tasks as it will NOT have a visible output eg through print")
print("daemon is enabled to true by default for loop")
print("daemon is enabled to false by default for start")
print("arguments will be [] by default")
print("time to end the loop task now")

t.stop()
```

### Development:
Install buildproj:

`pip install buildproj`

`build --build`

In case of the binary not working:

`python buildbinary.py --build`

All processes are automated except for the sign in for pip, please be sure to also change the version and name in `setup.py`