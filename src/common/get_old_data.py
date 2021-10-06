from os import walk, getcwd

import pandas as pd


def get_old_data():
    file_name_beginning = 'huzaro_output_full_'

    filenames = next(walk(getcwd()), (None, None, []))[2]
    filenames = [fn for fn in filenames if fn.startswith(file_name_beginning)]

    if not filenames:
        return None, None

    filenames.sort(reverse=True)
    latest = filenames[0]

    df = pd.read_excel(latest, header=0)
    df['Cena'] = pd.to_numeric(df['Cena'])

    file_name_date = latest.replace(file_name_beginning, '').replace('.xls', '')

    return pd.read_excel(latest, header=0, sheet_name="full"), file_name_date
