import time
import threading

def job1(msg, t=1):
    print("Current thread:", threading.current_thread())
    # print("Active threads:", threading.active_count())
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))

def job2(msg, t=5):
    print("Current thread:", threading.current_thread())
    # print("Active threads:", threading.active_count())
    print("Print message: {} is working.".format(msg))
    time.sleep(t)
    print("{} is done.".format(msg))


class multithread1:
    def __init__(self, input_list):
        self.data = input_list.copy()

    def get_data(self):
        return self.data

    def job1(self, data, idx):
        """
        Calculate the square number of all elements
        """
        print("Thread {} is starting.".format(idx))
        for j in range(len(data)):
            self.data[idx][j] = data[j]**2
            time.sleep(1)

    def run(self):
        all_thread = []

        # Create multi-thread
        for i in range(len(self.data)):
            thread = threading.Thread(target=self.job1, name="T{}".format(i), args=(self.data[i],i))
            
            thread.start()     # What is the difference?
            all_thread.append(thread)    
        
        # Temporately stop the main thread
        for thread in all_thread:
            # thread.start()     # What is the difference?
            thread.join()


