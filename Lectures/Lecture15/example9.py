"""
Example 9: Race Condition
"""

import multiprocessing as mp
import time

def job(value, num):
    for i in range(3):
        time.sleep(0.1) 
        value.value += num
        print(value.value, "Process: {}".format(mp.current_process()))
        
def multicore(num_process):
    x = mp.Value('i', 0)
    
    list_process = []

    for i in range(num_process):
        list_process.append(
            mp.Process(target=job, name="p{}".format(i), args=(x, 3*i))
        )
        list_process[i].start()
    
    for process in list_process:
        process.join()
    
if __name__ == '__main__':
    multicore(2)


