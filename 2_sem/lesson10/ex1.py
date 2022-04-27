import time

def heavy(n):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    time.sleep(1)

def sequential(n):
    for i in range(n):
        heavy(500)
    print(f"{n} циклов вычислений закончены")

if __name__ == "__main__":
    start = time.time()
    sequential(15)
    end = time.time()
    print("Общее время работы: ", end - start)