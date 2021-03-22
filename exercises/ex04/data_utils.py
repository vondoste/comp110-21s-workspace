"""Utility functions for wrangling data."""

__author__ = "730366999"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    # TODO 0.1) Complete the implementation of this function here.
    for row in csv_reader:
        rows.append(row)
    

    return rows


# TODO: Define the other functions here.
def column_values(input_table: list[dict[str, str]], column_name: str) -> list[str]:
    """Given a list of dictionaries and the name of a key, return a list of values for that key, same order in dictionary."""
    results: list[str] = []

    if len(input_table) > 0:
        for row in input_table:
            results.append(row[column_name])
    
    return results


def columnar(table_of_rows: list[dict[str, str]]) -> dict[str,list[str]]:
    """Convert a list of rows (list[dict[str,str]]) table into a dict of columns (dict[str, list[str]]) table."""
    results: dict[str, list[str]] = {}
    column_names: list[str] = table_of_rows[0].keys()

    for column in column_names:
        results[column] = column_values(table_of_rows, column)

    return results