import random
import threading
import time


lock = threading.Lock()


def file_read(file_name):
    lock.acquire()
    try:
        with open(file_name) as inf:
            print(inf.readlines())

        with open(file_name, 'w') as outf:
            outf.writelines([str(random.randint(0, 1000))])
        time.sleep(2)
    finally:
        lock.release()


if __name__ == "__main__":
    threads = []
    for thead in range(4):
        t = threading.Thread(target=file_read, args=('lol.txt',))
        threads.append(t)
        t.start()

    # Подождем, пока все потоки
    # завершат свою работу.
    for t in threads:
        t.join()
