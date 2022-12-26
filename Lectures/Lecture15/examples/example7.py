"""
Difference between mp.Pool.apply & mp.Pool.apply_async
"""

import multiprocessing as mp
import time
from jobs_mp import square


if __name__ == "__main__":
    # Pool.apply
    t = time.time()
    pool = mp.Pool()
    result1 = []
    for i in range(10):
        result1.append(pool.apply(square, (i,1)))         # It blocks until the result is ready
    print(result1)
    print("Execution time of example 7-1: {:.02f} sec.".format(time.time()-t))

    # Pool.apply_async
    t = time.time()
    pool = mp.Pool()
    result2 = []
    for i in range(10):
        result2.append(pool.apply_async(square, (i,1)))
    for res in result2:
        # Use method "get" to return the value
        print(res.get())
    print("Execution time of example 7-2: {:.02f} sec.".format(time.time()-t))

    # The end of the main scripts
    print("The END")

