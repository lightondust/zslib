from ast import literal_eval
import pandas as pd


def string_to_list_data(data):
    return literal_eval(data)


def string_to_list_series(data_series):
    return data_series.apply(string_to_list_data)


def string_to_list_dataframe(data_frame, column_name):
    data_frame[column_name] = string_to_list_series(data_frame[column_name])
    return data_frame


def dataframe_to_list_of_dict(data_frame):
    list_of_dict = []
    for idx, item in data_frame.iterrows():
        list_of_dict.append(item.to_dict())
    return list_of_dict


def csv_list_to_dataframe(file_list):
    review_df = pd.DataFrame()
    for file in file_list:
        review_df = review_df.append(pd.read_csv(file, index_col=0), ignore_index=True)
    return review_df
