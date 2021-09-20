from src.Classes.ErrorFile import File
from src.common.class_list_to_df import class_list_to_df
from src.common.compare_data import compare_data
from src.common.get_new_data import get_new_data
from src.common.get_old_data import get_old_data
from src.common.split_data import split_data
from src.common.xls_comparasion import xls_full_comparasion, xls_short_comparasion


def main():
    error_file = File('errors.txt')
    error_file.clean()

    input_data_file = File('huzaro_input.txt')
    input_data = input_data_file.read()

    prepared_data = split_data(input_data, error_file)
    new_data = get_new_data(prepared_data, error_file)
    new_data_df = class_list_to_df(new_data)
    old_data_df = get_old_data()

    merged_data = compare_data(new_data_df, old_data_df)

    xls_full_comparasion(merged_data)
    xls_short_comparasion(merged_data)


if __name__ == '__main__':
    main()
