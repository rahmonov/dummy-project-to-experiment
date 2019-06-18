import queue
from time import sleep
from urllib.request import urlopen
import threading

worker_data = ["http://google.com", "http://rahmonov.me", "http://bing.com"]

# load up a queue with your data, this will handle locking
q = queue.Queue()
for url in worker_data:
    q.put(url)


# define a worker function
def worker(url_queue):
    queue_full = True
    while queue_full:
        try:
            # get your data off the queue, and do some work
            url = url_queue.get(False)
            data = urlopen(url).read()
            sleep(1)
            print(f"{url}:", len(data))

        except queue.Empty:
            queue_full = False


# create as many threads as you want
thread_count = 3
for i in range(thread_count):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
