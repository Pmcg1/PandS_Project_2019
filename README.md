# Programming and Scripting 2019 Project
## G00190832 Peter McGowan

## Table of Contents
<!-- TOC -->
- [Introduction](#introduction)
    - [Background](#Background)
    - [Machine Learning](#Machine-Learning)
    - [Literature Review and Interesting Previous Analyses](#Literature-Review-and-Interesting-Previous-Analyses)
    - [Issues and Inconsistencies with Dataset](#Issues-and-Inconsistencies-with-Dataset)
- [License](#License)
- [Python Programmes](#Python-Programmes)
    - [Downloading the Repository](#Downloading-the-Repository)
    - [How to Run](#How-to-Run)
    - [Libraries Used](#Libraries-Used)
    - [Implementation](#Implementation)
    - [Investigations and Analysis](#Investigations-and-Analysis)
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

The data analysed by this programme is the "Iris Flower Data Set"<sup>[1](#myfootnote1)</sup>. R.A. Fisher collated and presented the data set in 1936 in his paper "The Use of Multiple Measurements in Taxonomic Problems"<sup>[2](#myfootnote2)</sup>. In this paper he studied the use of linear combinations of multiple characterising features of a species to discriminate it from related species. Fisher studied three related species of iris flowers in this paper:

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

Emerj.com defines "machine learning" as:
>[T]he science of getting computers to learn and act like humans do, and improve their learning over time in autonomous fashion, by feeding them data and information in the form of observations and real-world interactions.<sup>[3](#myfootnote3)</sup>

In the context of this project, we can state that machine learning involves the development of algorithms that can allow software to be trained (using training data) to recognise and classify data from real-world sources.

The data set has several characteristics that render it useful for machine learning applications, including but limited to the following:

- The Iris-setosa class is linearly separable from the other classes
- The Iris-versicolor and Iris-virginica classes are not linearly separable from each other
- It contains only 150 rows and 5 columns, therefore processing time for algorithms is relatively small
- The data set is made up of real data, made from careful observations by an expert - it has not been synthesised and can therefore be considered a fair representatino of the real world

Linear separability is an interesting in relation to the dataset, as the setosa observations can be easily distinguished from the versicolor and virginica observations<sup>[4](#myfootnote4)</sup>.

### Literature Review and Interesting Previous Analyses

A great many examples of analysis using the Iris Flower Data Set can be found online. Implementations in Python using various libraries are common, as are examples using other software packages.

#### Exploring the Iris Dataset - The Data Salaryman

"The data salaryman" presents an investigation into the data set using R (with the [tidyverse package](https://www.tidyverse.org/)) on Medium<sup>[5](#myfootnote5)</sup>. In addition to discussing the background and useful characteristics of the data set, he presents some basic visualisations (box & whisker plot and scatter plot) and then delves into three different algorithms for automated classification of data based on petal length and petal width:

- Decision Trees (~93% accuracy): Involves development of rules to cleanly divide data;
- Nearest Neighbour Clustering (>95% accuracy): Clustering of data based on training data;
- Support Vector Classsification (>95% accuracy): Clustering of data based on training data.

In keeping with the known characteristics of the data set, all algorithms explored had difficulty in distinguishing between the versicolor and virginica datasets in some incidences.

#### Basic Analysis of the Iris Data set Using Python - Oluwasogo Oluwafemi Ogundowole

Oluwasogo Oluwafemi Ogundowole demonstrates the use of pandas for managementn of the iris data set on Medium<sup>[6](#myfootnote6)</sup> and explores the tools of the [scikit-learn package](https://scikit-learn.org/stable/) (sklearn). He provides some basic viaualisations using matplotlib also.

The approach taken is to compare the following algorithms for machine learning:

- Logistic Regression (LR)
- Linear Discriminant Analysis (LDA)
- K-Nearest Neighbors (KNN)
- Classification and Regression Trees (CART)
- Gaussian Naive Bayes (NB)
- Support Vector Machines (SVM)

The findings were that the KNN algorithm was most accurate for making predictions, with an accuracy of ~90%. As expected, the setosa class is discriminated from the others 100% of the time.

#### Seaborn plot to visualize Iris data - Rakesh Kumar

Rakesh Kumar's python notebook on Kaggle<sup>[7](#myfootnote7)</sup> explores the use of the Seaborn library for python in visualising the data set.

He presents a range of seaborn plots to highlight characteristics of the data and has provided some inspiration for the visualisations used in this project.

#### Machine Learning with Iris Dataset - Jane Chen

Jane Chen on Kaggle<sup>[8](#myfootnote8)</sup> combines pandas, seaborn and sklearn in visualisation and analysis of the data set. She presents a pairplot and violin plots which demonstrate the characteristics of the data set. Following this she carries out classification of the data using the KNN algorithm. She presents two alternatives for selecetion of a training dataset and a testing dataset:

1. Train and test on the same dataset: 
    - Not preferred as it doesn't fit with the end goal of predicting previously unseen data
2. Split the dataset into a training set and a testing set:
    - Real observations will be used for both testing and training of the algorithm
    - No observations will appear in both datasets
    - Accuracy scores can vary depending on data selected

The article further explores the effect of the complexity (k value) used in the KNN algorithm.

### Issues and Inconsistencies with Dataset

It is noted that there are three inconsistencies between the data set sourced from  UCI<sup>[1](#myfootnote1)</sup> and the data set presented by Fisher<sup>[2](#myfootnote2)</sup>

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

- [Numpy](https://www.numpy.org/) - Used for a number of mathematical functions in the [iris_analysis.py](iris_analysis.py) programme;
- [Scipy](https://www.scipy.org/) - Used for certain statistical analysis functions in the [iris_analysis.py](iris_analysis.py) programme;
- [Pandas](https://pandas.pydata.org/) - Used for import, management, analysis and manipulation of data in the [iris_analysis.py](iris_analysis.py) and the [iris_visualisation.py](iris_visualisation.py) programme;
- [Matplotlib.pyplot](https://matplotlib.org/tutorials/introductory/pyplot.html) - Used for manipulation of elements of certain plots in the [iris_visualisation.py](iris_visualisation.py) programme;
- [Seaborn](https://seaborn.pydata.org/) - Used for creation and manipulation of all plots in the [iris_visualisation.py](iris_visualisation.py) programme. Seaborn extends the functionality of Matplotlib.

Please note that the programmes will not run successfuly if their required libraries are not installed.

### Implementation

Two separate python programmes have been written for investigation of the data set. These are discussed below.

[iris_analysis.py](iris_analysis.py): This 


[iris_visualisation.py](iris_visualisation.py: This


### Investigations and Analysis

## Results

### Tables

### Plots

#### Box & Whisker Plots

![Box & Whisker Plots](iris_boxplot.png)


#### Violin Plots

![Violin Plots](iris_violin.png)


#### Box & Whisker Plots vs Violin Plots

![Box & Whisker vs Violin Plots](iris_box_violin.png)


#### Histograms

![Distribution Plots](iris_dist.png)


#### Pairgrid

![Pairgrid Plot](iris_pairgrid.png)


## References

<a name="myfootnote1">1</a>: UCI Machine Learning Repository - Iris Data Set, http://archive.ics.uci.edu/ml/datasets/Iris  
<a name="myfootnote2">2</a>: The Use of Multiple Measurements in Taxonomic Problems, http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf  
<a name="myfootnote3">3</a>: emerj.com, What is Mschine Learning?, https://emerj.com/ai-glossary-terms/what-is-machine-learning/  
<a name="myfootnote4">4</a>: A Multithreaded Software Model for Backpropagation Neural Network Applications, 2.4.1 Linear Separability and the XOR Problem, http://www.ece.utep.edu/research/webfuzzy/docs/kk-thesis/kk-thesis-html/node19.html  
<a name="myfootnote5">5</a>: Exploring the Iris Dataset, https://medium.com/@livingwithdata/exploring-the-iris-dataset-260cc1e5cdf7  
<a name="myfootnote5">6</a>: Basic Analysis of the Iris Data set Using Python, https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342  
<a name="myfootnote5">7</a>: Seaborn plot to visualize Iris data, https://www.kaggle.com/rakesh6184/seaborn-plot-to-visualize-iris-data  
<a name="myfootnote5">8</a>: Machine Learning with Iris Dataset, https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset  
<a name="myfootnote5">9</a>:
<a name="myfootnote5">10</a>:
<a name="myfootnote5">11</a>:
<a name="myfootnote5">12</a>:


<sup>[1](#myfootnote1)</sup>



(https://towardsdatascience.com/a-guide-to-pandas-and-matplotlib-for-data-exploration-56fad95f951c)
(https://medium.com/@rayheberer/generating-matplotlib-subplots-programmatically-cc234629b648)

(https://stackoverflow.com/questions/23969619/plotting-with-seaborn-using-the-matplotlib-object-oriented-interface)


(https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
(https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
