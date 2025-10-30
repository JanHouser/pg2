import sys
import csv


def precti_hodnoty_a_incrementuj(file):

    all_results = []
    for line in file:
        data = line.split(',')
        result = []
        for value in data:
            value = value.strip().strip('"')
            try:
                value = int(value) + 1
            except ValueError:
                pass
            result.append(value)
        all_results.append(result)
    return all_results

if __name__ == "__main__":

    try:
        name = input("Zadej jmeno souboru: ")
        file = open(name, "r")
        results = precti_hodnoty_a_incrementuj(file)
        print(results)
    except FileNotFoundError:
        print(f'Soubor {name} neexistuje')

def zapis_data_do_csv(file_name, data):
    with open(file_name, "w") as file:
        for row in data:
            line = ','.join(row)
    data = precti_hodnoty_a_incrementuj(file)        




def nacti_csv(soubor):
    data = []
    fp = open(soubor)
    reader = csv.reader(fp)
    for row in reader:
        data.append(row)
    fp.close()
    return data


def spoj_data(data1, data2):
    print(data1)
    print(data2)
    header1 = data1[0]
    header2 = data2[0]
    header = set()
    header.update(header1)
    header.update(header2)
    print (header)


def zapis_csv(soubor, data):
    with open(soubor, "w") as fp:
        writer = csv.writer(fp)
        writer.writerows(data)


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        print(vysledna_data)
        zapis_csv("vysledny_excel.csv", vysledna_data)
    except IndexError:
        print("Nebyly zadany soubory")
    except FileNotFoundError:
        print("Soubor neexistuje")