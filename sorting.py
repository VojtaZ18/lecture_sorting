import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as soubor:
        data = csv.DictReader(soubor)
        slovnik = {}
        for row in data:
            for hlavicka, hodnota in row.items():
                if hlavicka not in slovnik:
                    slovnik[hlavicka] = [int(hodnota)]
                else:
                    slovnik[hlavicka].append(int(hodnota))
    return slovnik


def main():
    data = read_data("numbers.csv")
    print(data)


if __name__ == '__main__':
    main()
