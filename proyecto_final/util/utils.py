import os
def create_dir_files(dir_file):
    if not os.path.exists(dir_file):
        os.makedirs(dir_file)