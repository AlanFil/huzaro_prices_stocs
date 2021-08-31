import sys
from time import sleep
import requests
from scrapy import Selector
import xlwt
from tqdm import tqdm


def clean_errors_file():
    with open('error.txt', 'w') as f:
        f.write('')


def get_input_data():
    with open('huzaro_input.txt', 'r') as f:
        huzaro_input = f.read()

    return huzaro_input


def write_error(error_mes):
    print(error_mes)
    with open('error.txt', 'a', encoding='utf-8') as f:
        f.write(error_mes)

    print('Okno zostanie zamknięte w ciągu 15 sekund...')
    sleep(15)


def split_data(data_):
    data_ = data_.split('\n')

    for i, d in enumerate(data_):
        data_[i] = data_[i].split(',')

        if data_[i] == ['']:
            continue

        if len(data_[i]) != 2:
            write_error(f'Wystąpił błąd w linijce {i}\n')
            sys.exit()

    data_ = list(filter(lambda x: x != [''], data_))  # remove empty elements

    return data_


def main(data):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet 1')

    for i, (ean, link) in enumerate(tqdm(data, desc="Progress: ")):
        sel = Selector(text=requests.get(link.strip()).content)
        price = sel.xpath('//em[contains(@class, "main-price")]//text()').extract()[0]
        price = float(price.replace('\xa0', '').replace('zł', '').replace(',', '.'))
        price = price - (price * 0.15)
        price = format(price, '.2f')

        try:
            stock = sel.xpath('//div[@class="delivery"]/span[@class="second"]//text()').extract()[0]
        except IndexError:
            stock = sel.xpath('//div[@class="row availability"]/span[@class="second"]//text()').extract()[0]

        worksheet.write(i, 0, ean.strip())
        worksheet.write(i, 1, price)
        worksheet.write(i, 2, stock)

    workbook.save('huzaro_output.xls')


if __name__ == '__main__':
    clean_errors_file()
    huzaro_data = get_input_data()
    huzaro_data = split_data(huzaro_data)

    main(huzaro_data)
