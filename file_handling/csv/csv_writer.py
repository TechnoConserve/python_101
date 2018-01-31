import csv


def csv_dict_writer(data, path, fieldnames):
    """
    Writes a CSV file using DictWriter.
    :param data: Data to be written to output CSV file.
    :param path: File path to save output CSV file.
    :param fieldnames: Defines column/fieldnames.
    :return: None.
    """
    with open(path, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_writer(data, path):
    """
    Write data to a CSV file path.
    :param data: Data to be written as output CSV file.
    :param path: File path to save output CSV file.
    :return: None.
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow(line)


if __name__ == '__main__':
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    path = "output.csv"
    dict_path = "dict_output.csv"
    csv_writer(data, path)
    csv_dict_writer(my_list, dict_path, fieldnames)
