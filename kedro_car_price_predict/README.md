# Kedro Used Car Price Prediction with SQL / XLSX / CSV input

## Project

* This demo project is to showcase the compatibility of the Kedro with various input

## Datasets
There are 3 datasets for this project and are present in data -> 01_raw.

* mercedes: MySQL data from local server (NEED credential). It contains the used car price of Mercedes

* audi.csv: It contains the used car price of Audi with the information of the car

* hyundai.xlsx: It contains the used car price of Hyundai with the information of the car


## Pipeline Steps
* Load the datasets from SQL (MySQL) / CSV / XLSX (Openpyxl)
* Preprocess data files
* Combine data into one master data
* Split data into Train and test
* Train regression model on local machine
* Evaluate model performance
