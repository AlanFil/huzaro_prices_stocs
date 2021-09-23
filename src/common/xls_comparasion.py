import pandas as pd


def xls_full_comparasion(data, current_date):
    diff = data[(data['Cena'] != data['Cena stara']) | (data['Stan'] != data['Stan stary'])]

    with pd.ExcelWriter(f'huzaro_output_full_{current_date}.xls', engine='xlwt') as workbook:
        diff.to_excel(workbook, sheet_name='różnica')
        data.to_excel(workbook, sheet_name='full')


def xls_short_comparasion(data, current_date):
    try:
        short_version = data[(data['Cena'] != data['Cena stara']) | (data['Stan'] != data['Stan stary'])][['EAN', 'Cena', 'Stan']]
        short_version.to_excel(f'huzaro_output_short_{current_date}.xls',
                               engine='xlwt', index=False)
    except KeyError:
        data[['EAN', 'Cena', 'Stan']].to_excel(f'huzaro_output_short_{current_date}.xls',
                                               engine='xlwt', index=False)
