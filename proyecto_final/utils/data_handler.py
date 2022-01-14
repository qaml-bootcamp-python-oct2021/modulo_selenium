import csv
 
def get_data(filename):
    try:
        with open(filename,'r') as file:
            reader = csv.reader(file, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                return row
    except FileNotFoundError as fn:
        print(fn)


def get_data_lines(filename):
    lines=[]
    try:
        with open(filename,'r') as file:
            for line in file.readlines():
                lines.append(line[:-1])
            return lines
    except FileNotFoundError as fn:
        print(fn)