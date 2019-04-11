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

speciesList = df['species'].unique() # Extract unique species from species column
print(f'Species included are: {speciesList}') # Update to print without list format

# print(df)

print("Summary statistics for entire dataset:")
print(round(df.describe(percentiles=[]),3),'\n') # Summary statistics, rounded to 3 decimal places

def splitDataset(df, i):
    subdf = df.loc[df['species'] == i]
    print("Dataset created for: ", i)
    return subdf

#print(splitDataset(df,'setosa'))

for i in speciesList:
    #print(f'List of data for species: {i}')
    print(f'Summary statistics for {i} dataset:')
    currentdf = splitDataset(df, i)
    #print(subdf)
    print(round(currentdf.describe(percentiles=[]),3),'\n')

#df.plot(kind='box', subplots=True, layout=(2,2), grid = True, sharex = True, sharey= True) # Display box plots
#fig, axes = plt.subplots(nrows=2, ncols=2)
#fig.suptitle('Boxplots')


df.plot(kind='box', grid = True, sharex = True, sharey= True) # Display box plots
plt.title('combined dataset')
plt.show()


j = 1
for i in speciesList:
    plt.subplot(3,1,j)
    currentdf = splitDataset(df, i)
    currentdf.plot(kind='box', grid = True, sharex = True, sharey= True)
    plt.title(i)
    j = j+1

plt.show() # this section is currently broken



#df.plot(kind='hist', subplots=True, layout=(2,2), sharex=False, sharey = True, grid = True) # Display histograms

#scatter_matrix(df) # added basic scatter matrix but need to format

#plt.show()

# Edit to include scatter plot (and others?)
# Arrange all plots as subplots on one output
