# Project 2019
# Peter McGowan

# Visualisation of Iris Dataset

# Import pandas for managing data
# Import matplotlib.pyplot and seaborn for visualisation
#import numpy as np
import pandas as pd
#from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Importing and preparing data
f = pd.read_csv('iris.csv') # Import csv file using pandas
df = pd.DataFrame(f) # Create a dataframe from the csv data

# Create species-specific datasets for simplicity of visualisation
setosaSet = df.query("species == 'setosa'")
versiSet = df.query("species == 'versicolor'")
virgiSet = df.query("species == 'virginica'")

# Set style for Seaborn plots below
sns.set(style='darkgrid')

# Box and whisker plots
f, axes = plt.subplots(1, 4, sharey=False, figsize=(10, 8))

sns.boxplot(x='species',y='sepal_length',data=df, ax=axes[0])
sns.boxplot(x='species',y='sepal_width', data=df, ax=axes[1])
sns.boxplot(x='species',y='petal_length', data=df, ax=axes[2])
sns.boxplot(x='species',y='petal_width', data=df, ax=axes[3])



#plt.figlegend()


#Figure-level interface for drawing categorical plots onto a FacetGrid. (catplot)


plt.show()

#df.drop("Id", axis=1).boxplot(by="species", figsize=(10, 10))
#plt.show()


'''
g = sns.FacetGrid(df, col="species")

#sns.catplot(x="species", y="sepal_length", hue="species", kind="box", data=df, ax=axes[0])
#sns.catplot(x="species", y="sepal_width", hue="species", kind="box", data=df, ax=axes[1])
#sns.catplot(x="species", y="petal_length", hue="species", kind="box", data=df, ax=axes[2])
#sns.catplot(x="species", y="petal_width", hue="species", kind="box", data=df, ax=axes[3])

plt.show()
'''
'''
#df.plot(kind='box', subplots=True, layout=(2,2), grid = True, sharex = True, sharey= True) # Display box plots
#fig, axes = plt.subplots(nrows=2, ncols=2)
#fig.suptitle('Boxplots')


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