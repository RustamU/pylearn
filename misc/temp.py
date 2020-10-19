def benchmark(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print ('run time {}'.format (end-start))
        return func()
    return wrapper

@benchmark
def printList(a):
    for i in a:
        return i

a = [i for i in range (100000)]

printList(a)
