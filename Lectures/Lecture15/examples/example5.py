import multiprocessing as mp
from jobs_mp import job1, job2
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example 5")
    parser.add_argument("--num", default=None, type=int, help="Number of processes")

    opt= parser.parse_args()

    if opt.num is None:
        opt.num = mp.cpu_count()

    print("Example 5 has started.")

    print("CPU count:", mp.cpu_count())
    
    list_process = []

    for i in range(opt.num):

        if i%2 == 0:
            list_process.append(
                mp.Process(target=job1, args=("P{}".format(i),))
            )
        else:
            list_process.append(
                mp.Process(target=job2, args=("P{}".format(i),))
            )

        list_process[i].start()

    for process in list_process:
        process.join()

    print("Example 5 has finished.")

