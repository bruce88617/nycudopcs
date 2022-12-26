import multiprocessing as mp
import time

def job1(msg, t=1):
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))

def job2(msg, t=5):
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))

def square(num, t=1):
    time.sleep(t)
    return num*num

