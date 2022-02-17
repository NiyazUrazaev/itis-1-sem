import os

root_directory = '/Users/niyaz/PycharmProjects/itis-1-semester'
current_dir = os.path.join(root_directory, 'lesson2')
print(current_dir)
print(os.listdir(current_dir))

print(os.path.abspath('test1.py'))

for root, dirs, files in os.walk('/'):
    print(root, dirs, files)


