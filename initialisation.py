from download_data import download_excel
from read_data import read_folder
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

# Download all Excel files in 2024 from NHS to folder "data"
os.chdir("./data")
for month_num in range(1, 13):
    month_name = datetime(2024, month_num, 1).strftime("%B").lower()
    month_year = f"{month_name}-2024"
    download_excel(month_year)
os.chdir("..")

# Read all Excel files in folder "data" and save in datasets.xlsx
df = read_folder("./data")
df.to_excel("dataset.xlsx", index=False)

# download_excel("january-2024")
# download_excel("february-2024")
# download_excel("march-2024")
# download_excel("april-2024")
# download_excel("may-2024")
# download_excel("june-2024")
# download_excel("july-2024")
# download_excel("august-2024")
# download_excel("september-2024")
# download_excel("october-2024")
# download_excel("november-2024")
# download_excel("december-2024")
# download_excel("january-2025")