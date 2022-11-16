"""
Example 10: Lock
"""

import multiprocessing as mp
import time

def job(value, num, lock):
    # block the memory from other processes
    lock.acquire()
    for i in range(3):
        time.sleep(0.1) 
        value.value += num
        print(value.value, "Process: {}".format(mp.current_process()))
    # release the memory
    lock.release()
        
def multicore(num_process):
    x = mp.Value('i', 0)
    # Create a Lock
    l = mp.Lock()

    list_process = []

    for i in range(num_process):
        list_process.append(
            mp.Process(target=job, name="p{}".format(i), args=(x, 3*i, l))
        )
        list_process[i].start()
    
    for process in list_process:
        process.join()
    
if __name__ == '__main__':
    multicore(2)


