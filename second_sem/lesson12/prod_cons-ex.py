import random
import threading
import time
from queue import Queue

BUF_SIZE = 4
q = Queue(BUF_SIZE)


class ProducerThread(threading.Thread):
    def __init__(self, name):
        super(ProducerThread, self).__init__()
        self.name = name

    def run(self):
        while True:
            if not q.full():
                name = str(random.randint(1, 1000))
                q.put(name)
                print(f'Add to queue name {name}')


class ConsumerThread(threading.Thread):

    def run(self) -> None:
        while True:
            if not q.empty():
                name = q.get()
                print(f'Get name {name} from consumer')
                time.sleep(2)


p = ProducerThread(name='lol')
c = ConsumerThread()

p.start()
c.start()