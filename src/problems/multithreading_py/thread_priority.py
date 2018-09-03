import queue, threading, time


class MyThread(threading.Thread):
    def __init__(self, q, name):
        threading.Thread.__init__(self, name=name, daemon=True)
        self.q = q

    def run(self):
        print("Starting {}".format(self.name))
        while True:
            data = self.q.get()
            if data is None:
                break
            print("{} processing {}".format(self.name, data))
            time.sleep(2)
            self.q.task_done()
        print("Exiting {}".format(self.name))


thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["One", "Two", "Three", "Four", "Five"]

work_queue = queue.Queue()
threads = [MyThread(work_queue, t_name) for t_name in thread_list]
for thread in threads:
    thread.start()

for word in name_list:
    work_queue.put(word)
work_queue.join()

print("Main thread end!")
