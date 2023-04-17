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


def selection_sort(seznam, direction="vzestupne"):
    for i in range(len(seznam)):
        idx_extrem = i
        for j in range(i + 1, len(seznam)):
            idx_cislo = j
            if direction == "vzestupne":
                if seznam[idx_extrem] > seznam[idx_cislo]:
                    idx_extrem = idx_cislo
            elif direction == "sestupne":
                if seznam[idx_extrem] < seznam[idx_cislo]:
                    idx_extrem = idx_cislo
        seznam[i], seznam[idx_extrem] = seznam[idx_extrem], seznam[i]
    return seznam


def bubble_sort(seznam):
    for i in range(len(seznam) - 1):
        for idx in range(len(seznam) - i - 1):
            if seznam[idx] > seznam[idx + 1]:
                seznam[idx], seznam[idx + 1] = seznam[idx + 1], seznam[idx]
    return seznam



def main():
    data = read_data("numbers.csv")
    print(data)
    print(selection_sort(data["series_1"]))
    print(bubble_sort(data["series_2"]))


if __name__ == '__main__':
    main()
