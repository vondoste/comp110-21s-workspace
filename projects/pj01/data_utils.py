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
    """Given a list of dictionaries and the name of a key, return list of values for that key, same order in dict."""
    results: list[str] = []

    if len(input_table) > 0:
        for row in input_table:
            results.append(row[column_name])
    
    return results


def columnar(table_of_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert a list of rows (list[dict[str,str]]) table into a dict of columns (dict[str, list[str]]) table."""
    results: dict[str, list[str]] = {}
    column_names = table_of_rows[0].keys()  # Can't figure out what type to use for this variable.

    for column in column_names:
        results[column] = column_values(table_of_rows, column)

    return results


def head(table_of_columns: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first number_of_rows rows of data for each column."""
    results: dict[str, list[str]] = {}

    for column in table_of_columns.keys():
        temporary: list[str] = []
        holding_column: list[str] = table_of_columns[column]

        if len(holding_column) < number_of_rows:  # returns entire table if number_of_rows is > len of table
            number_of_rows = len(holding_column)

        for i in range(number_of_rows):
            temporary.append(holding_column[i])
        
        results[column] = temporary
    
    return results


def select(input_table: dict[str, list[str]], columns_wanted: list[str]) -> dict[str, list[str]]:
    """Returns a subset of the input_table that only contains the columns named in columns_wanted."""
    output_table: dict[str, list[str]] = {}
    for column in columns_wanted:
        output_table[column] = input_table[column]

    return output_table


def count(list_of_values: list[str]) -> dict[str, int]:
    """Given a list values, returns a dict with each unique value, and a count of how often it was in the list."""
    results: dict[str, int] = {}
    for value in list_of_values:
        if value in results:
            results[value] += 1
        
        else:
            results[value] = 1
    
    return results


def csv_in_column_distribution(input_list: list[str]) -> dict[str, int]:
    """Given a list of csv strings, will return a dictionary of counts for each unique value in the list"""
    results: dict[str, int] = {}
    for string in input_list:
        values: list[str] = string.split(", ")
        for item in values:
            if item in results.keys():
                results[item] += 1
            else:
                results[item] = 1
    return results


def csv_tally(input: list[str], mask: list[bool]) -> list[str]:
    """Given a list of csv values (str) and a list of bool, count how many values for every True, 0 for every False."""
    result: list[str] = []
    for i in range(len(input)):
        if mask[i]:
            result.append(str(len(input[i].split(","))))
        else:
            result.append("0")
    return result


def average_list(input: list[int]) -> float:
    """Given a list of integers, returns the average value of the list."""
    accumulator: int = 0
    for number in input:
        accumulator += number
    return accumulator / len(input)


def average_columns(input: dict[str, list[str]]) -> list[str]:
    """Given a dict of columns of numbers, return a list that is the mean of each row(index) while ignoring empty cells."""
    result: list[str] = []
    keys: list[str] = []
    for key in input.keys():
        keys.append(str(key))
    for i in range(len(input[keys[0]])):
        row_sum: int = 0
        row_count: int = 0
        for key in input.keys():
            if input[key][i] != '':  # Ignore empty fields
                row_count += 1
                row_sum += int(input[key][i])
        result.append(str(row_sum / row_count))

    return result


def not_none_mask(input: list[str]) -> list[bool]:
    output: list[bool] = []
    for line in input:
        if line == "None":
            output.append(False)
        else:
            output.append(True)
    return output


