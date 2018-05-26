import csv

import requests
from bs4 import BeautifulSoup

url = 'http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=1'

response = requests.get(url)
html_document = response.text
soup = BeautifulSoup(html_document, 'lxml')

select_part = soup.find('select', {'id': 'dwrNoList'})
option_part = select_part.find_all('option')

whole_number = []

for opt in option_part:
    whole_number.append(opt.text)

loop_url = 'http://nlotto.co.kr/gameResult.do?method=byWin&drwNo='

whole_list = []

f = open('./lotto2.csv', 'w', encoding='utf8')

fieldnames = ['회차', '1', '2', '3', '4', '5', '6', '7']
wr = csv.writer(f)
dictWriter = csv.DictWriter(f, fieldnames=fieldnames)



whole_array = []

for number in whole_number:
    number_dict = {}
    # if number == "800":
    #     break
    print(number)
    response = requests.get(loop_url + number)
    html_document = response.text

    soup = BeautifulSoup(html_document, 'lxml')

    number_part = soup.find('div', {'class': 'lotto_win_number'})
    with_numbers_p = number_part.find('p', {'class': 'number'})
    win_numbers = with_numbers_p.find_all('img')

    each_number_list = []

    huicha_dict = {}

    huicha_dict['회차'] = number
    i = 1
    for win in win_numbers:
        each_number_list.append(win.get('alt', ''))
        huicha_dict[i] = win.get('alt', '')
        i = i + 1
        # print(win.get('alt', ''))
    # print(number + "회차 \n")
    # print(each_number_list)
    whole_array.append(huicha_dict)

    number_dict[number] = each_number_list
    whole_list.append(number_dict)

dictWriter.writeheader()

print(whole_array)

csv_file = './lotto2.csv'
csv_columns = ['회차', 1, 2, 3, 4, 5, 6, 7]
dict_data = whole_array


def WriteDictToCSV(csv_file, csv_columns, dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                print(data)
                writer.writerow(data)

    except IOError:
        print("I/O error({0}): {1}".format(IOError.errno, IOError.strerror))
    return


WriteDictToCSV(csv_file, csv_columns, dict_data)
