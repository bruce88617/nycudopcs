"""
Example 3: Daemon thread
"""

import threading
from jobs_thread import job1, job2

# thread1 
thread1 = threading.Thread(target=job1, name="T1", args=("Thread 1",))

# thread2, will be automatically terminated when the MainThread is stopped.
thread2 = threading.Thread(target=job2, name="T2", args=("Thread 2",), daemon=True)

print("Current thread:", threading.current_thread())

print("="*50)
thread1.start()
thread2.start()
thread1.join()
# thread2.join()
print("="*50)

print("Current thread:", threading.current_thread())
print("Active threads:", threading.active_count())


print("All done!")
