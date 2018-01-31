import csv


def csv_writer(data, path):
    """
    Write data to a CSV file path.
    :param data: Data to be written as output CSV file.
    :param path: File path to save output CSV file.
    :return: Returns nothing.
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
    path = "output.csv"
    csv_writer(data, path)
