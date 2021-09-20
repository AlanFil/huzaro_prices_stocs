import pandas as pd


def compare_data(new_data, old_data):

    merged = pd.merge(new_data, old_data, on="EAN", how='left')
    merged['Różnica'] = merged['Cena_x'] - merged['Cena_y']
    output_df = merged[['EAN', 'Cena_x', 'Cena_y', 'Różnica', 'Stan_x', 'Stan_y', 'Nazwa_x', 'Uwagi_x']]
    output_df = output_df.rename(columns={'Cena_x': 'Cena nowa', 'Cena_y': 'Cena stara',
                                          'Stan_x': 'Stan nowy', 'Stan_y': 'Stan stary',
                                          'Nazwa_x': 'Nazwa', 'Uwagi_x': 'Uwagi'})

    return output_df
