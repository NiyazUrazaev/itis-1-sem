import threading
import time


def heavy(n, i, thead):
    for x in range(1, n):
        for y in range(1, n):
            x ** y
    time.sleep(1)
    print(f"Цикл № {i}. Поток {thead}")


def sequential(calc, thead):
    print(f"Запускаем поток № {thead}")
    for i in range(calc):
        heavy(500, i, thead)
    print(f"{calc} циклов вычислений закончены. Поток № {thead}")


def threaded(theads, calc):
    # theads - количество потоков
    # calc - количество операций на поток

    threads = []

    # делим вычисления на 4 потока
    for thead in range(theads):
        t = threading.Thread(target=sequential, args=(calc, thead))
        threads.append(t)
        t.start()

    # Подождем, пока все потоки
    # завершат свою работу.
    for t in threads:
        t.join()


if __name__ == "__main__":
    start = time.time()
    # разделим вычисления на 4 потока
    # в каждом из которых по 5 циклов
    threaded(3, 5)
    end = time.time()
    print("Общее время работы: ", end - start)