
def xls_full_comparasion(data, current_date):
    data.to_excel(f'huzaro_output_full_{current_date}.xls', engine='xlwt')


def xls_short_comparasion(data, current_date):
    short_version = data[(data['Cena'] != data['Cena stara']) | (data['Stan'] != data['Stan stary'])][['EAN', 'Cena', 'Stan']]
    short_version.to_excel(f'huzaro_output_short_{current_date}.xls', engine='xlwt')
