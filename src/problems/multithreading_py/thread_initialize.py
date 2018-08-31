import _thread
import time


def time_func(thread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{}: {}".format(thread, time.ctime(time.time())))


try:
    _thread.start_new_thread(time_func, ("Thread Number 1", 1))
    _thread.start_new_thread(time_func, ("Thread Number 2", 2))
except:
    print("Error, unable to initiate thread")

while True:
    pass
