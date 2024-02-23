from excel import (
    iter_read_excel_dataframes,
    split_columns,
    join_columns,
    explode_json_columns,
)
from scrap import url_to_soup, facebook
from scrap.conditions import run_conditions


def parse_dataframe(dataframe):
    dataframe = split_columns(
        dataframe,
        ["website"],
        separators=",",
        is_unique=True,
    )

    return dataframe


def scrap_dataframe(dataframe):
    def get_contact_info(websites):
        try:
            url = websites[0]
        except IndexError:
            return {}
        soup = url_to_soup(url)
        if soup:
            contact_info = run_conditions(
                soup.find_all("a", href=True), lambda x: x["href"]
            )
            if "facebook" in contact_info.keys():
                facebook_soup = url_to_soup(contact_info["facebook"])
                contact_info.update(
                    run_conditions(
                        facebook.scrap_contact_info_spans(facebook_soup),
                        lambda x: x.text,
                        to_skip=list(contact_info.keys()),
                    )
                )
            return contact_info

    dataframe["contact_info"] = dataframe["website"].apply(get_contact_info)
    dataframe = explode_json_columns(dataframe, ["contact_info"])
    return dataframe


def save_dataframe(dataframe, path, sheet_name):
    dataframe = join_columns(
        dataframe,
        ["website"],
        separators=",",
    )
    dataframe.to_excel(path, sheet_name=sheet_name)


if __name__ == "__main__":
    input_path = input("Enter path to input excel file:")
    output_path = input("Enter path to output excel file:")
    for sheet_name, dataframe in iter_read_excel_dataframes(input_path):
        dataframe = parse_dataframe(dataframe)
        dataframe = scrap_dataframe(dataframe)
        save_dataframe(dataframe, output_path, sheet_name)
