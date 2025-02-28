from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


def download_excel(month_year: str):
    """
    Download Excel given month and year
    :param month_year:
    :return:
    """
    link, filename = get_link_and_header(month_year)
    if link and filename:
        request_file(link, filename)


def get_link_and_header(month_year: str):
    """
    Get the hyperlink and name of Excel files on NHS given month and year
    :param month_year:
    :return:
    """
    driver = webdriver.Firefox()
    try:
        link = "https://digital.nhs.uk/data-and-information/publications/statistical/primary-care-dementia-data/" + month_year
        driver.get(link)

        query = "//a[@class='nhsd-a-box-link']"
        link_dataset = driver.find_elements(By.XPATH, query)
        link_dataset = [item.get_attribute("href") for item in link_dataset]

        query = "//p[@class='nhsd-t-heading-xs nhsd-!t-margin-bottom-2']"
        header_dataset = driver.find_elements(By.XPATH, query)
        header_dataset = [item.text for item in header_dataset]

        driver.quit()

        if not link_dataset or not header_dataset:
            raise IndexError("No link or header found on the page")

    except IndexError as e:
        print(f"Error occurred while fetching link and header: {e}")
        return None, None
    else:
        return link_dataset[0], header_dataset[0]


def request_file(link: str, filename: str):
    """
    Request the file from NHS given the link
    :param link:
    :param filename:
    :return:
    """
    file_url = link
    response = requests.get(file_url)
    if response.status_code == 200:
        name = filename.replace(":", "-") + ".xlsx"
        with open(name, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully as {name}")
    else:
        print(f"Failed to download. Status code: {response.status_code}")


