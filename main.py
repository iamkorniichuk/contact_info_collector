from excel import iter_read_excel_dataframes, split_columns, join_columns

if __name__ == "__main__":
    input_path = input("Enter path to input excel file:")
    output_path = input("Enter path to output excel file:")
    for sheet_name, dataframe in iter_read_excel_dataframes(input_path):
        dataframe = split_columns(
            dataframe,
            ["website"],
            separator=",",
            is_unique=True,
        )

        dataframe = join_columns(
            dataframe,
            ["website"],
            separator=",",
        )
        dataframe.to_excel(output_path, sheet_name=sheet_name)
