import requests
import threading
import time


def download_image(number):
    result_3 = requests.get(
        'https://reqres.in/img/faces/2-image.jpg',
    )
    with open(f'images/file{number}.jpg', 'wb') as file:
        file.write(result_3.content)


def split_threads(thread_number):
    for i in range(6):
        download_image(6 * thread_number + i)


start = time.time()
# Однопоточный вариант
# for i in range(30):
#     download_image(i)
# All done! Elapsed time is: 11.980262041091919

# Многопоточный вариант
threads_list = []
for i in range(5):
    thread_obj = threading.Thread(target=split_threads, args=(i,))
    thread_obj.start()
    threads_list.append(thread_obj)

for obj in threads_list:
    obj.join()

end = time.time()
print(f'All done! Elapsed time is: {end - start}')
# All done! Elapsed time is: 3.0007030963897705