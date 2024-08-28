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

def job3(value, num):
    for i in range(3):
        time.sleep(0.1) 
        value.value += num
        print(value.value, "Process: {}".format(mp.current_process()))

def job4(value, num, lock):
    # block the memory from other processes
    lock.acquire()
    for i in range(3):
        time.sleep(0.1) 
        value.value += num
        print(value.value, "Process: {}".format(mp.current_process()))
    # release the memory
    lock.release()

def job5(value, num, lock):
    # block the memory from other processes
    lock.acquire()
    for i in range(3):
        time.sleep(0.1) 
        value.value += num
        print(value.value, "Process: {}".format(mp.current_process()))
    # release the memory
    lock.release()

