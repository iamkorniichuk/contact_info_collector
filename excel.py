import pandas as pd
import numpy as np


def iter_read_excel_dataframes(path):
    excel_file = pd.ExcelFile(path)
    for sheet_name in excel_file.sheet_names:
        yield sheet_name, pd.read_excel(
            excel_file,
            sheet_name=sheet_name,
        )


def split_columns(dataframe, columns, separator=",", is_unique=False):
    def split(value):
        if value is np.nan:
            return []
        value = str(value).split(separator)
        if is_unique:
            value = set(value)
        return value

    for name in columns:
        dataframe[name] = dataframe[name].apply(lambda value: split(value))

    return dataframe


def join_columns(dataframe, columns, separator=","):
    def join(value):
        if value is np.nan:
            return ""
        return separator.join(value)

    for name in columns:
        if name in dataframe.columns:
            dataframe[name] = dataframe[name].apply(lambda value: join(value))

    return dataframe
