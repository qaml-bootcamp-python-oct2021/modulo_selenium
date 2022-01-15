import csv
from proyecto_final.util import config_init


def get_data(filename):
    print(f'{config_init.get_config().get_data_path()}/{filename}')
    try:
        with open(f'{config_init.get_config().get_data_path()}/{filename}', 'r') as file:
            data_list = []
            for data_item in file.readlines():
                data_list.append(data_item[:-1])
                print('****', data_item[:-1])
            return data_list
    except FileNotFoundError as fn:
        print(f'Error trying load data set: {fn}')


def get_data_csv(filename):
    file = open(f'{config_init.get_config().get_data_path()}/{filename}')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
        print(row,'**********')
    file.close()
    return rows
