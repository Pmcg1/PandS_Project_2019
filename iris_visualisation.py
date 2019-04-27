# Project 2019
# Peter McGowan

# Visualisation of Iris Dataset

# Import pandas for managing data
# Import matplotlib.pyplot and seaborn for visualisation
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing and preparing data
f = pd.read_csv('iris.csv') # Import csv file using pandas
df = pd.DataFrame(f) # Create a dataframe from the csv data


# Create species-specific datasets for simplicity of visualisation
setosaSet = df.query("species == 'setosa'")
versiSet = df.query("species == 'versicolor'")
virgiSet = df.query("species == 'virginica'")


# Extract various useful items from dataframe df for later use
dfCols = list(df.iloc[:, :-1]) # extract columns of dataframe to a list
n=len(dfCols) # length of dfCols
dfLabels = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)"] # Create more appropriate labels for columns


# Set style for Seaborn plots below
sns.set(style='darkgrid') # set the default style of the seaborn plots
sns.set_palette("colorblind",3) # set the default palette of the seaborn plots, 1 colour per species


# Box and whisker plots
fig, axes = plt.subplots(2, 2, figsize=(10, 10)) # Set up 2x2 grid for plots

i=0 # Set iterator to 0
ax00 = axes[0][0] # Create variables for each axis
ax01 = axes[0][1]
ax10 = axes[1][0]
ax11 = axes[1][1]

for ax in [ax00, ax01, ax10, ax11]: # for loop to run for each axes

    g = sns.boxplot(x="species", y=dfCols[i], data=df, ax=ax) # Box and whisker plots of each variable (iteratively) for each species
    g.set_ylabel(dfLabels[i]) # Extract the appropriate entry from the dfLabels list and apply to the plot
    i+=1 # Increment i

plt.tight_layout(rect=[0, 0, 1, 0.95]) # tight_layout to dynamically adjust space between elements, limit plots to 95% height to make space for title
plt.suptitle("Box & Whisker Plots by Attribute", fontsize = 20) # Title for overall plot
plt.savefig("iris_boxplot.png")  # save to named file


# Violin plots
fig, axes = plt.subplots(2, 2, figsize=(10, 10)) # Set up 2x2 grid for plots

i=0 # Set iterator to 0
ax00 = axes[0][0] # Create variables for each axis
ax01 = axes[0][1]
ax10 = axes[1][0]
ax11 = axes[1][1]

for ax in [ax00, ax01, ax10, ax11]: # for loop to run for each axes

    g = sns.violinplot(x="species", y=dfCols[i], data=df, ax=ax) # Box and whisker plots of each variable (iteratively) for each species
    g.set_ylabel(dfLabels[i]) # Extract the appropriate entry from the dfLabels list and apply to the plot
    i+=1 # Increment i

plt.tight_layout(rect=[0, 0, 1, 0.95]) # tight_layout to dynamically adjust space between elements, limit plots to 90% height to make space for title
plt.suptitle("Violin Plots by Attribute", fontsize = 20) # Title for overall plot
plt.savefig("iris_violin.png") # save to named file


# Combined Box and Violin Plots (orientation is switched from the separate plots above)
fig, axes = plt.subplots(4, 2, sharex=False, sharey=False, figsize=(10, 10)) # Set up 4x2 grid for plots

i=0 # Set iterator to 0

for i in range(n): # iterate over the number of elemnts in n (declared at line 24)

    g = sns.boxplot(y="species", x=dfCols[i], data=df, ax=axes[i, 0]) # box and whisker plot of each variable (iteratively)
    g = sns.swarmplot(y="species", x=dfCols[i], alpha=0.5, size=3, marker="D", color="red", data=df, ax=axes[i, 0]) # superimpose swarmplot on previous plot
    h = sns.violinplot(y="species", x=dfCols[i], inner="quartile", data=df, ax=axes[i, 1]) # violin plot of each variable (iteratively)
    g.set_xlabel(dfLabels[i]) # Extract the appropriate entry from the dfLabels list and apply to the left hand plot
    h.set_xlabel(dfLabels[i]) # Extract the appropriate entry from the dfLabels list and apply to the right hand plot
    h.yaxis.set_label_position("right") # move (subplot 2) labels to right hand side
    h.tick_params(length=0) # hide tick marks
    h.yaxis.set_ticks_position("right") # move (subplot 2) tick labels to right hand side

plt.tight_layout(rect=[0, 0, 1, 0.95]) # tight_layout to dynamically adjust space between elements, limit plots to 95% height to make space for title
plt.suptitle("Box & Whisker (with Swarm) Plots and Violin Plots Compared", fontsize = 20) # Title for overall plot
plt.savefig("iris_box_violin.png") # save to named file


# Distplot (Histograms)
fig, axes = plt.subplots(4, 1, sharex=False, sharey=False, figsize=(10, 10)) # Set up 1x4 grid for plots

i=0 # Set iterator to 0

for i in range(n): # iterate over the number of elemnts in n (declared at line 24)
    g = sns.distplot(setosaSet[dfCols[i]], rug=True, label='Setosa', ax=axes[i])
    g = sns.distplot(versiSet[dfCols[i]], rug=True, label='Versicolor', ax=axes[i])
    g = sns.distplot(virgiSet[dfCols[i]], rug=True, label='Virginica', ax=axes[i])
    g.set_xlabel(dfLabels[i]) 

plt.tight_layout(rect=[0, 0, 1, 0.92]) # tight_layout to dynamically adjust space between elements, limit plots to 92% height to make space for title and legend
plt.suptitle("Histograms for Each Variable, by Species", fontsize = 20) # Title for overall plot

handles, labels = g.get_legend_handles_labels() # Extract handles, labels from last iteration of plot loop
plt.figlegend(handles, labels, loc=1) # Create a figure legend and place at top right
plt.savefig("iris_dist.png") # save to named file


# Pairgrid - to show relationships between variables
g = sns.PairGrid(df, hue="species") # Create a pairgrid for df with each species displayed in a separate colour

g = g.map_diag(plt.hist, histtype="stepfilled") # plot histograms on the diagonals with "stepfilled" pattern
g = g.map_lower(sns.kdeplot) # plot kernal density estimate plots on the lower triangle
g = g.map_upper(plt.scatter, edgecolor="w", s=30) # plot scatterplots on the upper triangle. Edge coloured white and size set to 30 to make points stand out

labelDict = {'sepal_length': dfLabels[0], 
        'sepal_width': dfLabels[1], 
        'petal_length': dfLabels[2], 
        'petal_width': dfLabels[3]
        } # Create dict of df headers and match them to entries in the dfLabels list

i=0 # Set iterator to 0

for i in range(n): # For loop to replace dataframe headers with more appropriate labels
    g.axes[3, i].set_xlabel(dfLabels[i]) # set each x label on the bottom row to the i'th value of dfLabels
    g.axes[i, 0].set_ylabel(dfLabels[i]) # set each y label on the first column to the i'th value of dfLabels

g = g.add_legend() # add a legend from the last element generated
plt.tight_layout(rect=[0, 0, 0.90, 0.95]) # tight_layout to dynamically adjust space between elements, limit plots to 95% height to make space for title and 90% right to make space for legend
plt.suptitle("Pair Plot for Dataset", fontsize = 20) # Title for overall plot
plt.savefig("iris_pairgrid.png") # save to named file