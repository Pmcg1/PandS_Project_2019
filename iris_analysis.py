# Project 2019
# Peter McGowan

# Analysis of Iris Dataset

# Import numpy and pandas for analysis
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


f = pd.read_csv('iris.csv') # Import csv file using pandas

df = pd.DataFrame(f) # Create a dataframe from the csv data

# print(df)


print(round(df.describe(percentiles=[]),3)) # Summary statistics, rounded to 3 decimal places


df.plot(kind='box', subplots=True, layout=(2,2), grid = True, sharey= False) # Display box plots

df.plot(kind='hist', subplots=True, layout=(2,2), sharex=False, sharey = True, grid = True) # Display histograms

scatter_matrix(df) # added basic scatter matrix but need to format

plt.show()

# Edit to include scatter plot (and others?)
# Arrange all plots as subplots on one output
