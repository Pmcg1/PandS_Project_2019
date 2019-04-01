# Project 2019
# Peter McGowan

# Analysis of Iris Dataset

# Import numpy and pandas for analysis
import numpy as np
import pandas as pd


f = pd.read_csv('iris.csv') # Import csv file using pandas

df = pd.DataFrame(f) # Create a dataframe from the csv data

#print(df)

#print(f"Sepal Length: Max={df['sepal_length'].max()} Min={df['sepal_length'].min()} Mean={round(df['sepal_length'].mean(),2)} Median={df['sepal_length'].median()} StDev={round(df['sepal_length'].std(),2)}")
#print(f"Sepal Width: Max={df['sepal_width'].max()} Min={df['sepal_width'].min()} Mean={round(df['sepal_width'].mean(),2)} Median={df['sepal_width'].median()} StDev={round(df['sepal_width'].std(),2)}")
#print(f"Petal Length: Max={df['petal_length'].max()} Min={df['petal_length'].min()} Mean={round(df['petal_length'].mean(),2)} Median={df['petal_length'].median()} StDev={round(df['petal_length'].std(),2)}")
#print(f"Petal Width: Max={df['petal_width'].max()} Min={df['petal_width'].min()} Mean={round(df['petal_width'].mean(),2)} Median={df['petal_width'].median()} StDev={round(df['petal_width'].std(),2)}")

print(round(df.describe(percentiles=[]),3)) # Summary statistics, rounded to 3 decimal places