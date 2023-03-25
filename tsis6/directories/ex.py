import os
path = 'main_dir/second/file4.txt'

if os.path.exists(path):
    os.remove(path)
