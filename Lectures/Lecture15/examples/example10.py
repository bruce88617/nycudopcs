"""
Example 10: Lock
"""

import multiprocessing as mp
from jobs_mp import job4
        
def multicore(num_process):
    x = mp.Value('i', 0)
    # Create a Lock
    l = mp.Lock()

    list_process = []

    for i in range(num_process):
        list_process.append(
            mp.Process(target=job4, name="p{}".format(i), args=(x, 3*i, l))
        )
        list_process[i].start()
    
    for process in list_process:
        process.join()
    
if __name__ == '__main__':
    multicore(4)


