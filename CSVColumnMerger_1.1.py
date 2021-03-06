#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

"""CSVColumnMerger_1.1.py:
Source files:
    - CSV file with multiple columns with the same name

Exit file:
    - CSV with unique column names
"""
import csv

SOURCE_FILE = 'source.csv'
RESULT_FILE = 'result.csv'


def write_column_merged_file():
    """def write_column_merged_file()
    Description: Generates a new CSV file with unique column names.
    In:          Cap.
    Out:         RESULT_FILE.
    """
    source_column_names, result_column_names = extract_column_names()

    result_file = open(RESULT_FILE, 'w', encoding='utf-8')
    result_file_writer = csv.writer(result_file)
    result_file_writer.writerow(result_column_names)  # Column headers

    with open(SOURCE_FILE, 'r', encoding='utf-8') as source_file:
        source_reader = csv.reader(source_file)
        next(source_reader, None)

        for row in source_reader:
            result_row = setup_result_row(*result_column_names)
            for field in row:
                if field != "":
                    source_column_name = source_column_names[row.index(field)]
                    result_column_index = result_column_names.index(
                                                          source_column_name)
                    result_row = (result_row[:result_column_index] +
                                  result_row[result_column_index+1:])
                    result_row[
                      result_column_index:result_column_index] = [field]
            result_file_writer.writerow(result_row)

    result_file.close()


def setup_result_row(*result_column_names):
    """def setup_result_row(*result_column_names)
    Description: Creates with so many positions as unique column names
                 in RESULT_FILE filled with empty spaces.
    In:          List result_column_names.
    Out:         List result_row.
    """
    result_row = []
    for column in result_column_names:
        result_row.append("")

    return result_row


def extract_column_names():
    """extract_column_names
    Description: Creates two lists:
                     - source_column_names: contains the column names of
                                            SOURCE_FILE
                     - result_column_names: contains the columns of RESULT_FILE
    In:          None.
    Out:         Lists source_column_names and result_column_names.
    """
    with open(SOURCE_FILE, 'r', encoding='utf-8') as source_file:
        source_reader = csv.reader(source_file)
        source_rows = list(source_reader)
        source_column_names = source_rows[0]

        result_column_names = []
        [result_column_names.append(column_name)
         for column_name in source_column_names
         if column_name not in result_column_names]

    return source_column_names, result_column_names


if __name__ == '__main__':
    write_column_merged_file()
