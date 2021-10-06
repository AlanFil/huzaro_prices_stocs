import requests
from scrapy import Selector
from tqdm import tqdm

from src.Classes.HuzaroProduct import HuzaroProduct
from src.Classes.Secrets import Secrets


def get_new_data(data, error_file):
    new_products_data = []

    with requests.Session() as s:
        for i, (ean, link) in enumerate(tqdm(data)):
            link = link.strip()
            ean = ean.strip()

            s.post(Secrets.HUZARO_LOGIN_PAGE, Secrets.HUZARO_PAYLOAD)
            page_content = s.get(link).content
            sel = Selector(text=page_content)
            try:
                price = sel.xpath('//em[contains(@class, "main-price")]//text()').extract()[0]
                price = float(price.replace('\xa0', '').replace('zł', '').replace(',', '.'))
                price = price - (price * 0.10)
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
                price = -1
                remark = 'Ten produkt jest niedostępny.'
                error_file.append_error(f'\nBrak produktu ({i}) {ean} -- {link}')

            stock_val = 1 if remark == "Natychmiast" else 0

            product = HuzaroProduct(ean, price, stock_val, name, remark)
            new_products_data.append(product)

    return new_products_data
