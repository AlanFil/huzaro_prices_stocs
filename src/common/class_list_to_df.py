import pandas as pd


def class_list_to_df(data):
    value_list = [(product.ean, product.price, product.stock_val, product.name, product.remark) for product in data]

    data_df = pd.DataFrame.from_dict(value_list)
    data_df.columns = ['EAN', 'Cena', 'Stan', 'Nazwa', 'Uwagi']

    data_df['EAN'] = pd.to_numeric(data_df['EAN'])
    data_df['Cena'] = pd.to_numeric(data_df['Cena'])

    return data_df
