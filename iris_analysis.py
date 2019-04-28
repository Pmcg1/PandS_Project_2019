# Project 2019
# Peter McGowan

# Analysis of Iris Dataset

# Import pandas for managing data
# Import numpy and scipy.stats for analysis
import numpy as np
from scipy import stats
import pandas as pd

# Importing and preparing data  
f = pd.read_csv('iris.csv') # Import csv file using pandas
df = pd.DataFrame(f) # Create a dataframe from the csv data

# General analysis of contents of dataset
speciesList = df['species'].unique() # Extract unique species from species column
print('Species included in this dataset are: ')
for i in speciesList: # For loop to list the species in the dataset
    print ('* ', i)
print() # Blank line for formatting

print('Information about the imported dataset: ')
print(df.info(verbose=True, memory_usage=False, null_counts=False),'\n')  # pandas.DataFrame.info with memory_usage and null_counts parameters excluded

print('Records for each species:')
print(df['species'].value_counts(),'\n') # pandas.series.value_counts to count the no. of records for each species

print('Sample of data (First 5 records):')
print(df.head(n=5),'\n') # pandas.DataFrame.head with the number set to 5, to show first 5 records as a sample of the dataset

print('Sample of data (Random 5 records):')
print(df.sample(n=5),'\n') # pandas.DataFrame.sample with the number set to 5, to show a random 5 records as a sample of the dataset

# Statistical Analysis of overall Dataset
print("Summary statistics for the dataset:")
print(round(df.describe(percentiles=[]),3),'\n') # Summary statistics, rounded to 3 decimal places

# Statistical Analysis of Dataset by Species
def speciesStats(species): # Function that can be called on subsets of the dataset
   print(f'Detailed statistical analysis for species: {species.iloc[0,4]}')  # f-string that uses the iloc function to seek the first value in the species column as a descriptor for the subset
   measColumns = species.columns[0:4] # Create a list of the 4 measured attributes, extracted from the subset
   statDF = pd.DataFrame(data = None, columns = measColumns, index = ['Min', 'Max', 'Median', 'Mean', 'Variance', 'StDev', 'Range', 'Skewness', 'Kurtosis']) # Create a new dataframe. Date is initialised as None as this will be called repeatedly. columns and index are declared.

   for i in measColumns:
      column = species.loc[:,i] # column in the current column of data sliced from the subset using .loc iteratively
      columnDict =	{ # Create a dict that includes a number of statistics generated, rounded to 3 decimal places where necessary for clarity
         "Min": np.min(column), # numpy minimum
         "Max": np.max(column), # numpy maximum
         "Median": np.median(column), # numpy median
         "Mean": round(np.mean(column),3), # numpy mean
         "Variance": round(np.var(column),3), # numpy variance
         "StDev": round(np.std(column),3), # numpy standard deviation
         "Range": (np.max(column)-np.min(column)), # range using numpy max and min
         "Skewness": round(stats.skew(column),3), # scipy.stats skewness
         "Kurtosis": round(stats.kurtosis(column),3) # scipy.stats kurtosis
      }
      statDF[i].update(pd.Series(columnDict)) # Update the statDF dataframe (empty) values with the dict generated on this iteration
   print(statDF, '\n')

for i in speciesList: # Will loop through each element in the speciesList series
   speciesDF = df.query("species == @i") # Select the i'th species for this iteration
   speciesStats(speciesDF) # Call the speciesStats function for this iteration