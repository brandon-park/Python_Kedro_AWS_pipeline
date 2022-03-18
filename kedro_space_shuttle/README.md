
# Kedro Spaceflights AWS Sagemaker Implementation
# Scenario
It is 2160 and the space tourism industry is booming. Globally, there are thousands of space shuttle companies taking tourists to the Moon and back.

## Project
Construct a model for predicting the price for each trip to the Moon and the corresponding return flight

## Datasets
There are 3 datasets for this project and are present in data -> 01_raw.

companies.csv gives a list of the companies, their location and respective ratings
for the space expedition. 

reviews.csv gives ratings for different shuttles on various parameters like comfort, price, crew and so on.

shuttles.xlsx gives a list of shuttles, the base location, engine structure and cost for a space trip


## Pipeline Steps
* Load the datasets
* Preprocess data files
* Combine data into one master data
* Split data into Train and test
* Train regression model on Sagemaker
* Untar model
* Evaluate model performance



## Visualization
![viz1](https://github.umn.edu/park2599/kedro_aws_pipeline/blob/master/kedro_viz/viz1.JPG)
![viz1](https://github.umn.edu/park2599/kedro_aws_pipeline/blob/master/kedro_viz/viz2.JPG)



## Citation
The demo makes use of concepts and example explained in https://aws.amazon.com/blogs/opensource/using-kedro-pipelines-to-train-amazon-sagemaker-models/ .
In addition, we have borrowed the dataset and implementation procedure from below:
@software{Alam_Kedro_2021,
author = {Alam, Sajid and Bălan, Lorena and Comym, Gabriel and Dada, Yetunde and Danov, Ivan and Hoang, Lim and Kanchwala, Rashida and Klein, Jiri and Milne, Antony and Schwarzmann, Joel and Theisen, Merel and Wong, Susanna},
month = {12},
title = {{Kedro}},
url = {https://github.com/quantumblacklabs/kedro},
version = {0.17.6},
year = {2021}
}




