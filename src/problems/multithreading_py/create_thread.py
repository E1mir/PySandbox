import threading
import time

exit_flag = False


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting {}".format(self.name))
        time_func(self.name, self.counter, 3)
        print("Exiting {}".format(self.name))


def time_func(thread, delay, counter):
    while counter:
        if exit_flag:
            thread.exit()
        time.sleep(delay)
        print("{}: {}".format(thread, time.ctime(time.time())))
        counter -= 1


if __name__ == '__main__':
    thread_1 = MyThread(1, "Thread 1", 1)
    thread_2 = MyThread(1, "Thread 2", 2)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Exit main thread")
