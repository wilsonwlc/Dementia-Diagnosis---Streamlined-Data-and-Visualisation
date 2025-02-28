import os.path
import pandas as pd
import schedule
import time
from datetime import datetime
from calendar import monthrange
from download_data import download_excel
from read_data import read_excel, extract_month, extract_year, combine_excel


def schedule_job():
    job_download()
    job_update_data()
    schedule.every().day.do(job_download)
    schedule.every().day.do(job_update_data)
    while True:
        schedule.run_pending()
        time.sleep(28800)


def job_download():
    if check_last_day():
        month_year = generate_suffix_month_year()
        os.chdir("./data")
        download_excel(month_year)
        os.chdir("..")


def job_update_data():
    if check_last_day():
        try:
            month_year = generate_suffix_month_year()
            filename = suffix_to_filename(month_year)
            path = os.path.join("./data", filename)
            df_last_month = read_excel(path)
            df_master = pd.read_excel("dataset.xlsx")
            df = combine_excel(df_master, df_last_month)
            df.to_excel("dataset.xlsx", index=False)
            month = extract_month(month_year).capitalize()
            year = extract_year(month_year)
            print(f"Master dataset updated successfully for {month} {year}")
        except FileNotFoundError as e:
            print(f"Error occur when updating data: {e}")


def generate_suffix_month_year():
    today = datetime.now()
    current_year = today.year
    last_month_date = today.replace(day=1)
    if last_month_date.month == 1:
        last_month_date = last_month_date.replace(year=current_year - 1, month=12)
    else:
        last_month_date = last_month_date.replace(month=last_month_date.month - 1)
    last_month_name = last_month_date.strftime("%B").lower()
    suffix = f"{last_month_name}-{current_year}"
    return suffix


def suffix_to_filename(month_year: str):
    year = extract_year(month_year)
    month = extract_month(month_year).capitalize()
    return f"Primary Care Dementia Data, {month} {year}- Summary.xlsx"


def check_last_day():
    today = datetime.now()
    _, last_day = monthrange(today.year, today.month)
    if today.day == last_day:
        return True
    else:
        return False


if __name__ == "__main__":
    schedule_job()

