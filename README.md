# Programming and Scripting 2019 Project
## G00190832 Peter McGowan

## Table of Contents
<!-- TOC -->
- [Introduction](#introduction)
    - [Background](#Background)
    - [Machine Learning](#Machine Learning)
    - [Literature Review and Interesting Previous Analyses](#Literature-Review-and-Interesting-Previous-Analyses)
    - [Issues and Inconsistencies with Dataset](#Issues-and-Inconsistencies-with-Dataset)
- [License](#License)
- [Python Programmes](#Python-Programmes)
    - [Downloading the Repository](#Downloading-the-Repository)
    - [How to Run](#How-to-Run)
    - [Libraries Used](#Libraries-Used)
    - [Implementation](#Implementation)
- [Results](#Results)
    - [Tables](#Tables)
    - [Plots](#Plots)
- [References](#References)
<!-- /TOC -->  

## Introduction

This analysis of Fisher's Iris Flower Data Set has been carried out as an assignment of the Programming & Scripting module of the Higher Diploma In Data Analytics at GMIT. The project description can be found [here](https://github.com/ianmcloughlin/project-pands/blob/master/project.pdf).

The project repository contains the following files:

File | Description
-----| -----------
LICENSE | License for project (Apache 2.0)
README.md | This file - description of project and instructions
iris.csv | Iris Flower Data Set
iris_analysis.py | Python Programme for carrying out analysis of Iris Dataset
iris_visualisation.py | Python Programme for creating visualisations from Iris Dataset
iris_boxplot.png | Output from iris_visualisation.py - Box & Whisker Plot
iris_violin.png | Output from iris_visualisation.py - Violin Plot
iris_box_violin.png | Output from iris_visualisation.py - Comparison of Box & Whisker Plot and Violin Plot
iris_dist.png | Output from iris_visualisation.py - Histogram
iris_pairgrid.png |  Output from iris_visualisation.py - Pairgrid Plot

### Background

The data analysed by this programme is the "Iris Flower Data Set". R.A. Fisher collated and presented the data set in 1936 in his paper "The Use of Multiple Measurements in Taxonomic Problems". In this paper he studied the use of linear combinations of multiple characterising features of a species to discriminate it from related species. Fisher studied three related species of iris flowers in this paper:

- Iris setosa
- Iris versicolor
- Iris virginica

Fifty samples of each species were analysed, with the data for Iris setosa and Iris versicolor having been provided by his then-colleague, Botanist Edgar Anderson, from a study of a single colony.

Fisher studied four characteristics of each species:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Machine Learning

****What is machine learning??????****

The data set has several characteristics that render it useful for machine learning applications:

- The Iris-setosa class is linearly separable from the other classes
- The Iris-versicolor and Iris-virginica classes are not linearly separable from each other

*****ADD MORE TO THIS****

### Literature Review and Interesting Previous Analyses

A great many examples of analysis using the Iris Flower Data Set can be found online. Implementations in Python using various libraries are common, as are examples using other packages such as R.


*****ADD MORE TO THIS****


### Issues and Inconsistencies with Dataset

It is noted that there are three inconsistencies between the data set sourced from  [UCI](http://archive.ics.uci.edu/ml/datasets/Iris) and the dataset presented by [Fisher](http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf):

1. 35th sample: the fourth feature is given as "0.1" where Fisher had originally given "0.2".
2. 38th sample: the second feature is given as "3.1" where Fisher had originally given "3.6".
3. 38th sample: the third feature is given as "1.5" where Fisher had originally given "1.4".

These three errors have not been rectified in the dataset analysed.

## License

This project is licensed under the Apache License 2.0 - see [LICENSE.md](LICENSE) for details.

## Python Programmes

### Downloading the Repository

The repository is stored at [https://github.com/Pmcg1/PandS_Project_2019](https://github.com/Pmcg1/PandS_Project_2019).

To download it, do the following:

1. Click on the "Clone or Download" button
2. Select "Download ZIP". This will open a prompt allowing you to save the file to your computer.
3. Navigate to the download location and extract the compressed (.zip) folder to a suitable location.

### How to Run

Once you have downloaded the folder, you will need to ensure that you are running it in the correct environment. This software has been written using Python 3.7.1, it will require a Python version of 3.7 at a minimum to run as designed. This project also requires a number of external Python libraries ([listed below](#Libraries-Used)).
I recommend that you download the Anaconda distribution of Python 3.7 from the [downloads section](https://www.anaconda.com/distribution/#download-section) of the Anaconda Website.

Once the correct version of Python has been installed, running either of the included programmes can be carried out as follows:

1. Open a command prompt (cmd) or equivalent on your PC. The alternative "cmder" programme ([available here](https://cmder.net/)) is recommended.
2. Navigate to the drive that the programme is on by typing the drive letter followed by :.
3. Navigate to the correct folder using the "cd" command.
4. Run the programme by typing the following:

> python <programme_name.py>

### Libraries Used

- [Numpy](https://www.numpy.org/) - Used for a number of mathematical functions in the [iris_analysis.py](iris_analysis.py) programme. 
- [Scipy](https://www.scipy.org/) - Used for certain statistical analysis functions in the [iris_analysis.py](iris_analysis.py) programme. 
-[Pandas](https://pandas.pydata.org/) - Used for import, management, analysis and manipulation of data in the [iris_analysis.py](iris_analysis.py) and the [iris_visualisation.py](iris_visualisation.py) programme. 
- [Matplotlib.pyplot](https://matplotlib.org/tutorials/introductory/pyplot.html) - Used for manipulation of elements of certain plots in the [iris_visualisation.py](iris_visualisation.py) programme.
- [Seaborn](https://seaborn.pydata.org/) - Used for creation and manipulation of all plots in the [iris_visualisation.py](iris_visualisation.py) programme. Seaborn extends the functionality of Matplotlib.

Please note that the programmes will not run successfuly if their required libraries are not installed.

### Implementation

### Investigations and Analysis

## Results

### Tables

### Plots

- Box & Whisker Plots
- Violin Plots
- Box & Whisker Plots vs Violin Plots
- Histograms
- Pairgrid

## References

<a name="myfootnote1">1</a>: UCI Machine Learning Repository - Iris Data Set, http://archive.ics.uci.edu/ml/datasets/Iris,
<a name="myfootnote1">2</a>: The Use of Multiple Measurements in Taxonomic Problems, http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf,
<a name="myfootnote1">3</a>:
<a name="myfootnote1">4</a>:
<a name="myfootnote1">5</a>:



<sup>[1](#myfootnote1)</sup>

(https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
(https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
(https://medium.com/@livingwithdata/exploring-the-iris-dataset-260cc1e5cdf7)
(https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset)
(https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)
(https://towardsdatascience.com/a-guide-to-pandas-and-matplotlib-for-data-exploration-56fad95f951c)
(https://medium.com/@rayheberer/generating-matplotlib-subplots-programmatically-cc234629b648)
(https://www.kaggle.com/rakesh6184/seaborn-plot-to-visualize-iris-data)
(https://stackoverflow.com/questions/23969619/plotting-with-seaborn-using-the-matplotlib-object-oriented-interface)
(http://www.ece.utep.edu/research/webfuzzy/docs/kk-thesis/kk-thesis-html/node19.html)