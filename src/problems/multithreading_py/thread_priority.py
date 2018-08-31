import queue
import threading

exit_flag = False


class MyThread(threading.Thread):

    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("Starting {}".format(self.name))
        process_data(self.name, self.q)
        print("Exiting {}".format(self.name))


def process_data(working_thread, q):
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print("{} processing {}".format(working_thread, data))


thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["One", "Two", "Three", "Four", "Five"]

queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
t_id = 1

for t_name in thread_list:
    thread = MyThread(t_id, t_name, work_queue)
    thread.start()
    threads.append(thread)
    t_id += 1

queue_lock.acquire()
for word in name_list:
    work_queue.put(word)
queue_lock.release()

while not work_queue.empty():
    pass

exit_flag = True

for t in threads:
    t.join()
print("Exit main thread")
