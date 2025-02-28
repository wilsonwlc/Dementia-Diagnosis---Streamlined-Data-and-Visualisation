# Dementia Diagnoses Dashboard
## Overview
This project provides an automated pipeline for downloading and updating dementia diagnoses data from the NHS, processing the data, and visualizing it using an interactive dashboard built with Dash and Plotly.

The data is downloaded automatically every month, combined with existing data, and updated into a master dataset (`dataset.xlsx`). The Dash application allows users to explore and visualize the data, with features such as age-group filtering, tables, and interactive trend graphs.

## Features
* Automated Data Download: Every month, new datasets are automatically downloaded from the NHS and appended to the master dataset (`dataset.xlsx`).
* Interactive Dashboard: An interactive dashboard built with Dash to visualize the data, including:
    * Dropdown to select age groups.
    * Data table to display the number of diagnoses by gender (Male, Female).
    * Line graph showing trends of dementia diagnoses over time.
* Data Update: The dashboard updates automatically every month when new data is added to the master file.

## Technologies Used
* Python: For scripting, data processing, and backend logic.
* Dash: For building the interactive web application.
* Plotly: For creating interactive charts.
* Selenium: For web scraping to download the data.
* Pandas: For data manipulation and analysis.
* Schedule: For scheduling monthly tasks to download and process data.

## Project Structure
* `data/` - Folder to store the downloaded datasets
* `dataset.xlsx` - Master dataset containing all dementia diagnoses data
* `download_data.py` - Script to download the data from NHS website
* `read_data.py` - Script to read and process the downloaded data
* `schedule_job.py` - Script that schedules tasks to download and update data
* `analyse_data.py` - Dash application for visualizing the data


## Installation
To get started with this project, follow the steps below
### Prerequisites
Make sure you have the following installed:
* Python 3.x
* pip (Python package manager)
### Step 1: Clone the Repository
Clone the repository to your local machine.
```bash
git clone https://github.com/your-username/Dementia-Diagnoses-Dashboard.git
cd Dementia-Diagnoses-Dashboard
```
### Step 2: Install Dependencies
Manually install the following dependencies
```bash
pip install pandas dash plotly selenium schedule
```
### Step 3: Install Firefox & Geckodriver
Since Selenium is used for downloading data, ensure that you have:
* Firefox installed ([Download here](https://www.mozilla.org/en-US/firefox/new/))
* Geckodriver installed ([Download here](https://github.com/mozilla/geckodriver/releases))

Ensure geckodriver is in your system's PATH.

## Running the Project
### 1. Download and Process Initial Data
Run the following script to download all available data for 2024 and create `dataset.xlsx`:
```bash
python initialisation.py
```
### 2. Start the Scheduled Data Update
To automatically download and update the data every month, run:
```bash
python schedule_job.py
```
### 3. Launch the Dashboard
To run the Dash web application:
``` bash
python analyse_data.py
```
Then open http://127.0.0.1:8050/ in your browser.


## Usage
* Interactive Dashboard:
    * Select an age group from the dropdown.
    * View the data table displaying diagnoses by gender and month.
    * Analyse trends using the line chart.
* Automatic Data Update:
    * The dataset is updated automatically every month when new data is downloaded.






