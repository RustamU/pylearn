import os

NUM_PROC  = 5
children = []

for process in range(NUM_PROC):
    pid = os.fork()
    if pid > 0:
        print("This is the parent process {}".format(os.getpid()))
        children.append(pid)
    else:
        print("This is the child process {}".format(os.getpid()))
        os._exit(0)

for i, proc in enumerate(children):
    os.waitpid(proc, 0)

print("Parent process is closing")
