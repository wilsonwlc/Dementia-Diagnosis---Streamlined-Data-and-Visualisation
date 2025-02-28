import pandas as pd
import os
import re


def combine_excel(df1, df2):
    """
    Combine and sort 2 data frames
    :param df1:
    :param df2:
    :return:
    """
    df = pd.concat([df1, df2], ignore_index=True)
    df = df.drop_duplicates().sort_values(by=["year", "month_num", "age_gp"])
    return df


def read_folder(path_folder):
    """
    Read all Excel files given the path of a folder
    :param path_folder:
    :return:
    """
    filenames = os.listdir(path_folder)
    all_dfs = []
    for filename in filenames:
        path = os.path.join(path_folder, filename)
        df = read_excel(path)
        all_dfs.append(df)
    combined_df = pd.concat(all_dfs, ignore_index=True)
    combined_df = combined_df.sort_values(by=["year", "month_num", "age_gp"])
    return combined_df


def read_excel(filename):
    """
    Read an Excel file given filename
    :param filename:
    :return:
    """
    df = pd.read_excel(io=filename, sheet_name="Table 2", skiprows=9, nrows=12).drop("_", axis=1).rename(columns={"Unnamed: 0": "age_gp"})
    df["year"] = int(extract_year(filename))
    df["month"] = extract_month(filename)
    df["month_num"] = pd.to_datetime(df["month"], format="%B").dt.month
    return df


def extract_year(filename: str):
    pattern = r'(\d{4})'
    match = re.search(pattern, filename)
    return match.group(1) if match else None


def extract_month(filename: str):
    pattern = r'(january|february|march|april|may|june|july|august|september|october|november|december)'
    match = re.search(pattern, filename, re.IGNORECASE)
    return match.group(1).lower() if match else None


