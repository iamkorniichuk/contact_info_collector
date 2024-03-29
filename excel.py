from regex import split_by_punctuation

import pandas as pd
import numpy as np


def iter_read_excel_dataframes(path):
    excel_file = pd.ExcelFile(path)
    for sheet_name in excel_file.sheet_names:
        yield sheet_name, pd.read_excel(
            excel_file,
            sheet_name=sheet_name,
        )


def split_columns(dataframe, columns, separators=",", is_unique=False):
    def split(value):
        if value is np.nan:
            return []
        value = split_by_punctuation(str(value), separators)
        if is_unique:
            value = list(set(value))
        return value

    for name in columns:
        dataframe[name] = dataframe[name].apply(lambda value: split(value))

    return dataframe


def join_columns(dataframe, columns, separators=","):
    def join(value):
        if value is np.nan:
            return ""
        return separators.join(value)

    for name in columns:
        if name in dataframe.columns:
            dataframe[name] = dataframe[name].apply(lambda value: join(value))

    return dataframe


def explode_json_columns(dataframe, columns):
    for name in columns:
        if name in dataframe.columns:
            dataframe = dataframe.join(pd.json_normalize(dataframe.pop(name)))
    return dataframe
