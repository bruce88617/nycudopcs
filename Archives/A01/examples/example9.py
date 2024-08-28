"""
Example 9: Race Condition
"""

import multiprocessing as mp
from jobs_mp import job3
        
def multicore(num_process):
    x = mp.Value('i', 0)
    
    list_process = []

    for i in range(num_process):
        list_process.append(
            mp.Process(target=job3, name="p{}".format(i), args=(x, 3*i))
        )
        list_process[i].start()
    
    for process in list_process:
        process.join()
    
if __name__ == '__main__':
    multicore(4)


