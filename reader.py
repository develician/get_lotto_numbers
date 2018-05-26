import csv


def ReadCSVasDict(csv_file):
    whole_array = []
    try:
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                whole_array.append(row['1'])
                whole_array.append(row['2'])
                whole_array.append(row['3'])
                whole_array.append(row['4'])
                whole_array.append(row['5'])
                whole_array.append(row['6'])
                whole_array.append(row['7'])
        # print(whole_array)
        seen = set()
        uniq = []
        for x in whole_array:
            if x not in seen:
                uniq.append(x)
                seen.add(x)
        print(seen)
        print(uniq)
        # for el in whole_array:

        # print(set([x for x in whole_array if whole_array.count(x) > 1]))
    except IOError:
        print("I/O error({0}): {1}".format(IOError.errno, IOError.strerror))
    return


csv_file = './lotto2.csv'

ReadCSVasDict(csv_file)

