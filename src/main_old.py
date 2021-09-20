import sys
import requests
import xlwt
from time import sleep
from scrapy import Selector
from tqdm import tqdm

from src.Classes.HuzaroWorksheet import HuzaroWorksheet


def clean_errors_file():
    with open('../error.txt', 'w') as f:
        f.write('')


def get_input_data():
    with open('../huzaro_input.txt', 'r') as f:
        huzaro_input = f.read()

    return huzaro_input


def write_error(error_mes, close=False):
    print(error_mes)
    with open('../error.txt', 'a', encoding='utf-8') as f:
        f.write(error_mes)

    if close:
        print('Okno zostanie zamknięte w ciągu 15 sekund...')
        sleep(15)
        sys.exit()


def split_data(data_):
    data_ = data_.split('\n')

    for i, d in enumerate(data_):
        data_[i] = data_[i].split(',')

        if data_[i] == ['']:
            continue

        if len(data_[i]) != 2:
            write_error(f'Wystąpił błąd w linijce {i}\n', close=True)

    data_ = list(filter(lambda x: x != [''], data_))  # remove empty elements

    return data_


def main(data):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet 1')

    ws = HuzaroWorksheet(worksheet)
    ws.initiate_worksheet()

    for i, (ean, link) in enumerate(tqdm(data)):
        link = link.strip()
        ean = ean.strip()
        sel = Selector(text=requests.get(link).content)
        try:
            price = sel.xpath('//em[contains(@class, "main-price")]//text()').extract()[0]
            price = float(price.replace('\xa0', '').replace('zł', '').replace(',', '.'))
            price = price - (price * 0.15)
            price = format(price, '.2f')
        except IndexError:
            price = sel.xpath('//div[@class="alert-error alert"]/p//text()').extract()[0]

        name = ''.join(sel.xpath('//h1[@class="name"]//text()').extract()).strip()

        if not price == 'Ten produkt jest niedostępny.':
            try:
                remark = sel.xpath('//div[@class="delivery"]/span[@class="second"]//text()').extract()[0]
            except IndexError:
                remark = sel.xpath('//div[@class="row availability"]/span[@class="second"]//text()').extract()[0]
        else:
            remark = 'Niedostępny'
            write_error(f'\nBrak produktu ({i}) {ean} -- {link}')

        stock_val = 1 if remark == "Natychmiast" else 0

        ws.write(i+1, 0, ean)
        ws.write(i+1, 1, price)
        ws.write(i+1, 2, stock_val)
        ws.write(i+1, 3, name)
        ws.write(i+1, 4, remark)

    workbook.save('huzaro_output.xls')


# if __name__ == '__main__':
#     clean_errors_file()
#     huzaro_data = get_input_data()
#     huzaro_data = split_data(huzaro_data)
#
#     main(huzaro_data)
