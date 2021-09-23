import pandas as pd
import numpy as np


def compare_data(new_data, old_data):

    merged = pd.merge(new_data, old_data, on="EAN", how='left')
    merged['Różnica cena'] = merged['Cena_x'] - merged['Cena_y']
    merged['Zmiana stanu'] = np.where(merged['Stan_x'] != merged['Stan_y'], True, False)
    output_df = merged[['EAN', 'Cena_x', 'Cena_y', 'Różnica cena',
                        'Stan_x', 'Stan_y', 'Zmiana stanu', 'Nazwa_x', 'Uwagi_x']]
    output_df = output_df.rename(columns={'Cena_x': 'Cena', 'Cena_y': 'Cena stara',
                                          'Stan_x': 'Stan', 'Stan_y': 'Stan stary',
                                          'Nazwa_x': 'Nazwa', 'Uwagi_x': 'Uwagi'})

    return output_df
