# Project 2019        Programming and Scripting
This repository consists of my analysis of the Fisher's Iris Dataset as specified in the final project [Link to Project](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

# How to download this repository
1. Logon to GitHub [GitHub Homepage](https://github.com/gabrielmulligan/fishersirisdataset)
2. Click the download button
3. To run the code, ensure you have Python installed

# Fisher's Iris Dataset

## Introduction
Fisher's Iris data set is a multivariate data set introduced by Ronald Fisher in 1936, as an example of linear discriminant analysis i.e. a method used in statistics to find a linear combination of features that characterizes or separates two or more classes of objects or events.

## The Data
The data was collected by Fisher’s colleague, Edgar Anderson, in order to quantify the scientific variation of Iris flowers of three related species. Two of the three species (setosa and versicolor) were collected in the Gaspé Peninsula in Quebec, Canada "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus" [1](https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2).
The data set consists of fifty samples from each of three species of Iris (setosa, versicolor and virginica). Four features were measured (in cm) from each sample:-
* Length of Petal
* Width of Petal
* Length of Sepal* (the firm green part that supports the petal once it has bloomed) 
* Width of Sepal
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

## Statistical Summary

### Setosa
This details the mean (average), standard deviation and min/max (incl. 25%/50%/75% percentiles) of the data for the Iris Setosa

|      |Sepal Length|Sepal Width|Petal Length|Petal Width|
| --- | --- | --- |--- | --- |
| Count | 50 | 50 | 50 | 50 |
| Mean | 5.006 | 3.418 | 1.464 | 0.244 |
| Std Deviation | 0.35249 | 0.381024 |0.173511 | 0.10721 |
| Min | 4.3 | 2.3 |1.0 | 0.1 |
| 25th percentile | 4.8 | 3.125 |1.4 | 0.2 |
| 50th percentile | 5.0 | 3.4 |1.5 | 0.2 |
| 75th percentile | 5.2 | 3.675 |1.575 | 0.3 |
| Max | 5.8 | 4.4 |1.9 | 0.6 |

### Versicolor

### Virginica

## Scatterplot Diagrams

These are the scatterplot diagrams

![Scatterplot Diagrams of Fisher's Iris Dataset]()

## Findings

Iris Setosa is linearly separable from the other two, while there is considerable overlap between Iris Virginica and Iris Versicolor, as can be seen from both figures in the Scatterplot diagrams from the Python program below.

# Python Program (fisher_scatterplot.py)

This outputs a statistical analysis (mean,min,max,standard deviation) of the Iris Dataset and plots the findings of the 150 samples into a scatterplot diagram to highlight specific patterns in the two diagrams.





## plot.py (to be run from iPython prompt) contains the solution to Problem 10
This solution imports the numpy and matplotlib modules, then uses the arange to define the required range and then plots the functions as specified in the problem set.

# REFERENCES
I used the following online resources in compiling the solution outlined above, including researching how to code scatterplot diagrams in Python, specifically Reference 2 - Abhishek Gupta on kaggle - which greatly helped explain how the data and features are setup in order to correctly create the diagrams once the pro


* 1. [Source Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems. Ann. Eugenics 7, Pt. II, 179-188. As found here](https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2)
* 2. [Abhishek Gupta's analysis of the Fisher Dataset on kaggle](https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation)
* 3. [An overview of the Iris Dataset from Codebag NG incl. some programs to help analyze it](https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)
* 4. [Edukast's Youtube video on Machine Learning Classification - specifically using Fisher's Iris Dataset](https://www.youtube.com/watch?v=wIubuU7gejM)
* 5. [Dr. Ian McLoughlin's GMIT lectures](https://web.microsoftstream.com/video/6db924ef-af13-47da-a620-0e5b59e1c0ff)
* 6. [Writing readme.md files on Github](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
* 7. [Creating tables in markdown](https://www.makeuseof.com/tag/create-markdown-table/)
