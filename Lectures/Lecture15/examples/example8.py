import multiprocessing as mp
import time


def square(num, t=1):
    time.sleep(t)
    return num**2


if __name__ == "__main__":
    # Use mp.Pool to return the value
    t = time.time()
    pool = mp.Pool()
    result1 = pool.map(square, range(10))
    print(result1)
    print("Execution time of example 8-1: {:.02f} sec.".format(time.time()-t))

    # Without multiprocessing
    t = time.time()
    pool = mp.Pool()
    result2 = []

    result2.append(pool.map_async(square, range(10)))
    
    for res in result2:
        print(res.get())
    print("Execution time of example 8-2: {:.02f} sec.".format(time.time()-t))

