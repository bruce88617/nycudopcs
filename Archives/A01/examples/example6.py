import multiprocessing as mp
import time
from jobs_mp import square


if __name__ == "__main__":
    
    # Use mp.Process
    t = time.time()
    
    print("Example 6-1 has started.")

    num_process = mp.cpu_count()
    list_process = []

    for i in range(num_process):
        list_process.append(
            mp.Process(target=square, args=(i,))
        )

        list_process[i].start()

    for process in list_process:
        process.join()

    print("Example 6-1 has finished.")
    print("Execution time of example 6-1: {:.02f} sec.".format(time.time()-t))
 
    # Use mp.Pool.map to return the value
    t = time.time()
    print("Example 6-2 has started.")
    pool = mp.Pool(mp.cpu_count())
    result1 = pool.map(square, range(10))
    print(result1)
    print("Execution time of example 6-2: {:.02f} sec.".format(time.time()-t))

    # Without multiprocessing
    t = time.time()
    print("Example 6-3 has started.")
    result2 = []
    for i in range(10):
        result2.append(square(i))

    print(result2)
    print("Execution time of example 6-3: {:.02f} sec.".format(time.time()-t))

