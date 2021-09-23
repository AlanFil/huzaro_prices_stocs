import os

from src.Classes.ErrorFile import File
from src.common.class_list_to_df import class_list_to_df
from src.common.compare_data import compare_data
from src.common.current_date import current_date
from src.common.get_new_data import get_new_data
from src.common.get_old_data import get_old_data
from src.common.split_data import split_data
from src.common.xls_comparasion import xls_full_comparasion, xls_short_comparasion


def main():
    error_file_name = 'errors.txt'
    input_data_file_name = 'huzaro_input.txt'

    error_file = File(error_file_name)
    error_file.clean()

    input_data_file = File(input_data_file_name)
    input_data = input_data_file.read()

    prepared_data = split_data(input_data, error_file)
    new_data = get_new_data(prepared_data, error_file)
    new_data_df = class_list_to_df(new_data)
    old_data_df, file_name_date = get_old_data()

    if old_data_df is None:
        output_data = new_data_df
    else:
        output_data = compare_data(new_data_df, old_data_df)

    current_date_for_file_name = current_date()  # to make same date in both files
    xls_full_comparasion(output_data, current_date_for_file_name)
    xls_short_comparasion(output_data, current_date_for_file_name)

    if file_name_date and current_date_for_file_name != file_name_date:
        os.remove(f'huzaro_output_full_{file_name_date}.xls')
        os.remove(f'huzaro_output_short_{file_name_date}.xls')


if __name__ == '__main__':
    main()
