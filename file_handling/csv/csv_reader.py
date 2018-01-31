import csv


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    :param file_obj: File object to parse.
    :return: Returns first and last names of each line in the file object.
    """
    reader = csv.DictReader(file_obj)
    for line in reader:
        print(line['first_name'])
        print(line['last_name'])


if __name__ == '__main__':
    with open('names.csv') as f_obj:
        csv_dict_reader(f_obj)
