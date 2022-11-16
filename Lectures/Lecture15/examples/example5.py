import multiprocessing as mp
import time

def job1(msg, t=1):
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))

def job2(msg, t=5):
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))


if __name__ == "__main__":
    print("Example 5 has started.")

    num_process = 4
    list_process = []

    for i in range(num_process):

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

