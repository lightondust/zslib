from ast import literal_eval
import pandas as pd


def string_to_list_data(data):
    return literal_eval(data)


def string_to_list_column(data_series):
    return data_series.apply(string_to_list_data())


def csv_list_to_dataframe(file_list):
    review_df = pd.DataFrame()
    for file in file_list:
        review_df = review_df.append(pd.read_csv(file, index_col=0), ignore_index=True)
    return review_df
