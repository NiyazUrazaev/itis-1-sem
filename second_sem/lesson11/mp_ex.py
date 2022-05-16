import os
import time
from multiprocessing import Pool, Process, Value, Array, freeze_support

# def f(x):
#     return x*x
#
# if __name__=='__main__':
#     # 2.5 sec
#     array = [1, 2, 3]*10**7
#     start = time.time()
#     # list(map(f, array))
#
#     freeze_support()
#     with Pool(processes=4) as p:
#         p.map(f, array)
#
#     print(time.time() - start)



# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
#
# if __name__=='__main__':
#     freeze_support()
#     print(f'MAIN PID: {os.getpid()}')
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()





def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__=='__main__':
    freeze_support()

    num = Value('d', 0.0)
    arr = Array('i', range(10))
    print(num.value)
    print(arr[:])
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])