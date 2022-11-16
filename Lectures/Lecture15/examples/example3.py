"""
Example 3: Daemon thread
"""


import threading
import time

def job1(msg, t=1):
    # print("Current thread:", threading.current_thread())
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))

def job2(msg, t=5):
    # print("Current thread:", threading.current_thread())
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))

# thread1 
thread1 = threading.Thread(target=job1, name="T1", args=("Thread 1",))

# thread2, will be automatically terminated when the MainThread is stopped.
thread2 = threading.Thread(target=job2, name="T2", args=("Thread 2",), daemon=True)

print("Current thread:", threading.current_thread())

print("="*50)
thread1.start()
thread2.start()
print("="*50)

print("Current thread:", threading.current_thread())
print("Active threads:", threading.active_count())


print("All done!")
