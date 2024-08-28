"""
Example 11: Semaphore
"""

import multiprocessing as mp
from jobs_mp import job5
        
def multicore(num_process):
    x = mp.Value('i', 0)
    # Create a semaphore, set the maximum concurrent processes is 2
    l = mp.Semaphore(2)

    list_process = []

    for i in range(num_process):
        list_process.append(
            mp.Process(target=job5, name="p{}".format(i), args=(x, 3*i, l))
        )
        list_process[i].start()
    
    for process in list_process:
        process.join()
    
if __name__ == '__main__':
    multicore(4)


