import time

def timer(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        return res, t2 - t1
    return wrapper
