from os import walk, getcwd
import pandas as pd
import xlrd


def get_old_data():
    filenames = next(walk(getcwd()), (None, None, []))[2]
    filenames = [fn for fn in filenames if fn.startswith("huzaro_output")]

    if not filenames:
        return None

    filenames.sort(reverse=True)
    latest = filenames[0]

    df = pd.read_excel(latest, header=0)
    df['Cena'] = pd.to_numeric(df['Cena'])

    return pd.read_excel(latest, header=0)
