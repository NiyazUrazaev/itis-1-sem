import os, shutil

src_file = os.path.abspath('in.txt')

next_file = os.path.abspath('next/out.txt')

shutil.copyfile(src_file, next_file)