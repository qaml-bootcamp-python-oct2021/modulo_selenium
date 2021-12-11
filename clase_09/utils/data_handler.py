
def get_data(filename):
    try:
        with open(filename,'r') as file:
            return file.readlines()
    except FileNotFoundError as fn:
        print(fn)