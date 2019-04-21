# Project 2019
# Peter McGowan

# Analysis of Iris Dataset

# Import numpy and pandas for analysis
import numpy as np
from scipy import stats
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Importing and preparing data
f = pd.read_csv('iris.csv') # Import csv file using pandas

df = pd.DataFrame(f) # Create a dataframe from the csv data

# General analysis of contents of dataset
speciesList = df['species'].unique() # Extract unique species from species column
print('Species included in this dataset are: ')
for i in speciesList:
    print ('* ', i)
print()

print('Information about the imported dataset: ')
print(df.info(verbose=True, memory_usage=False, null_counts=False),'\n')

print('Records for each species:')
print(df['species'].value_counts(),'\n')

print('Sample of data (First 5 records):')
print(df.head(n=5),'\n')

print('Sample of data (Random 5 records):')
print(df.sample(n=5),'\n')

print("Summary statistics for the dataset:")
print(round(df.describe(percentiles=[]),3),'\n') # Summary statistics, rounded to 3 decimal places



# Statistical Analysis of Dataset by Species

#print(setosaSet.loc[:,'sepal_width'])



def speciesStats(species):
   print(f'Detailed statistical analysis for species: {species.iloc[0,4]}')  
   measColumns = species.columns[0:4]
   statDF = pd.DataFrame(data = None, columns = measColumns, index = ['Min', 'Max', 'Median', 'Variance', 'StDev', 'Skewness', 'Kurtosis'])

   for i in measColumns:
      column = species.loc[:,i]
      columnDict =	{
         "Min": np.min(column),
         "Max": np.max(column),
         "Median": np.median(column),
         "Mean": round(np.mean(column),3),
         "Variance": round(np.var(column),3),
         "StDev": round(np.std(column),3),
         "Skewness": round(stats.skew(column),3),
         "Kurtosis": round(stats.kurtosis(column),3)
      }
      statDF[i].update(pd.Series(columnDict))
   print(statDF, '\n')

for i in speciesList:
   speciesDF = df.query("species == @i")
   speciesStats(speciesDF)


# Create species-specific datasets
#setosaSet = df.query("species == 'setosa'")
#versiSet = df.query("species == 'versicolor'")
#virgiSet = df.query("species == 'virginica'")



#for i in speciesList:
    #print(f'List of data for species: {i}')
 #   print(f'Summary statistics for {i} dataset:')
 #   currentdf = splitDataset(df, i)
    #print(subdf)
 #   print(round(currentdf.describe(percentiles=[]),3),'\n')


#df.plot(kind='box', subplots=True, layout=(2,2), grid = True, sharex = True, sharey= True) # Display box plots
#fig, axes = plt.subplots(nrows=2, ncols=2)
#fig.suptitle('Boxplots')

'''
# Set style for Seaborn plots below
sns.set(style='darkgrid')

# Set up figure for axis level plots
#f, ax = plt.subplots(figsize=(8, 8))
#ax.set_aspect("equal")


# Axis level vs figure level functions - review!!!

g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species", col="species", data=df, height=6, aspect=.4, x_jitter=.1)

g = sns.FacetGrid(df, hue="species", height=6)
g.map(plt.scatter, "sepal_length", "sepal_width", alpha=.7)
g.add_legend()

g = sns.FacetGrid(df, hue="species", height=6)
g.map(plt.scatter, "petal_length", "petal_width", alpha=.7)
g.add_legend()

# Jointplots - split per species?
sns.jointplot(x='sepal_length',y='sepal_width',data=df, height=5 )
sns.jointplot(x='petal_length',y='petal_width',data=df, height=5)


#a=sns.pairplot(df, hue="species", palette="colorblind", )
#sns.despine()
#a.fig.suptitle("Relationship between the variables for each species")
plt.show()


#df.plot(kind='hist', subplots=True, layout=(2,2), sharex=False, sharey = True, grid = True) # Display histograms

#scatter_matrix(df) # added basic scatter matrix but need to format

#plt.show()

# Edit to include scatter plot (and others?)
# Arrange all plots as subplots on one output
'''