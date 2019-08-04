from ast import literal_eval


def string_to_list_data(data):
    return literal_eval(data)


def string_to_list_column(data_series):
    return data_series.apply(string_to_list_data())
