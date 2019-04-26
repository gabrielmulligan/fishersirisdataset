# Project 2019        Programming and Scripting
This repository consists of my analysis of the Fisher's Iris Dataset as specified in the 2019 Project [Link to Project Detail PDF ](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

# How to download this repository
1. Logon to GitHub to locate my specific repository dedicated to this Project [My repository for this project on GitHub](https://github.com/gabrielmulligan/fishersirisdataset)
2. Click the download button.
3. To run the code, ensure you have Python installed.

# Fisher's Iris Dataset

## Introduction
Fisher's Iris data set is a multivariate data set introduced by Ronald Fisher in 1936, as an example of *linear discriminant analysis* i.e. a method used in statistics to find a linear combination of features that characterizes or separates two or more classes of objects or events. 
In this case, Fisher wished to investigate if the species of an Iris flower could be identified by examining its petal and sepal length and width.

## The Data
The data was collected by Fisher’s colleague, Edgar Anderson, in order to quantify the scientific variation of Iris flowers of three related species. Two of the three species (setosa and versicolor) were collected in the Gaspé Peninsula in Quebec, Canada  
>all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus <sup>[Reference 1](https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2)</sup>.

The data set consists of fifty samples from each of three species of Iris (setosa, versicolor and virginica). Four features were measured (in cm) from each sample:-
- Length of Petal
- Width of Petal
- Length of Sepal* (i.e. the firm green part that supports the petal once it has bloomed) 
- Width of Sepal
Based on the combination of these four features, Fisher developed a *linear discriminant model* (defined above) to distinguish the species from each other.

## Statistical Summary Tables

These tables detail the mean (average), standard deviation and min/max (incl. 25%/50%/75% percentiles) of the data for the three Iris species, as collected and documented by Edgar Anderson.

### Setosa

| IRIS SETOSA |Sepal Length|Sepal Width|Petal Length|Petal Width|
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

| IRIS VERSICOLOR |Sepal Length|Sepal Width|Petal Length|Petal Width|
| --- | --- | --- |--- | --- |
| Count | 50 | 50 | 50 | 50 |
| Mean | 5.936 | 2.77 | 4.26 | 1.326 |
| Std Deviation | 0.516171 | 0.313798 |0.469911 | 0.197753 |
| Min | 4.9 | 2.0 |3.0 | 1.0 |
| 25th percentile | 5.6 | 2.525 |4.0 | 1.2 |
| 50th percentile | 5.9 | 2.8 |4.35 | 1.3 |
| 75th percentile | 6.3 | 3.0 |4.6 | 1.5 |
| Max | 7.0 | 3.4 |5.1 | 1.8 |

### Virginica

| IRIS VIRGINICA |Sepal Length|Sepal Width|Petal Length|Petal Width|
| --- | --- | --- |--- | --- |
| Count | 50 | 50 | 50 | 50 |
| Mean | 6.588 | 2.974 | 5.552 | 2.026 |
| Std Deviation | 0.63588 | 0.322497 |0.551895 | 0.27465 |
| Min | 4.9 | 2.2 |4.5 | 1.4 |
| 25th percentile | 6.225 | 2.8 |5.1 | 1.8 |
| 50th percentile | 6.5 | 3.0 |5.55 | 2.0 |
| 75th percentile | 6.9 | 3.175 |5.875 | 2.3 |
| Max | 7.9 | 3.8 |6.9 | 2.5 |

## Scatterplot Diagrams

These are the scatterplot diagrams showing the distribution of a) Sepal Length and Width and b) Petal Length and Width across the three species of Iris.

![Figure 1: Scatterplot Diagrams of Fisher's Iris Dataset](https://github.com/gabrielmulligan/fishersirisdataset/blob/master/Fisher_Scatterplots.png)

and a summary of the main statistics of the dataset, per species:-

![Figure 2: Tabular Summary of the Primary Statistics of each Iris species](https://github.com/gabrielmulligan/fishersirisdataset/blob/master/Fisher_Summary.png)


# Findings

From the scatterplot diagrams above, **Iris Setosa is linearly separable from the other two**, while there is considerable overlap between Iris Virginica and Iris Versicolor, as can be seen from both figures in the Scatterplot diagrams from the Python program below.
Iris Setosa is seperable by the fact that its *Petal Length and Width* are significantly less than the other two species. Setosa's petal length ranges from 1.0-1.9cm and petal width from 0.1-0.6cm, substantially less than Versicolor's (Len 3.0-5.1cm and Wid 1.0-1.8cm) and Virginica's (Len 4.5-6.9cm and Wid 1.4-2.5cm). Visually, the Setosa is a much smaller flower, compared to the other two species.

|      |Setosa|Versicolor|Virginica|
| --- | --- | --- |--- |
| Min Petal Length | *1.0* | 3.0 |4.5 |
| Max Petal Length| *1.9* | 5.1 |6.9 |
| | |  | |
| Min Petal Width| *0.1* | 1.0 |1.4 |
| Max Petal Width| *0.6* | 1.8 |2.5 |

# Python Program 
## fisher_scatterplot.py

This outputs both a statistical analysis (mean,min,max,standard deviation) of the Iris Dataset using the `describe` function and plots the findings of the 150 samples into a scatterplot diagram to highlight specific patterns in the two diagrams. Both outputs are shown in the Figures above.

# REFERENCES
I used the following online resources in compiling the solution outlined above, including researching how to code scatterplot diagrams in Python, specifically Reference 2 - Abhishek Gupta on kaggle.com - which greatly helped explain how the arrays and features of a dataset are setup in order to accurately create scatterplot diagrams once the program runs.


1. [Source Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems. Ann. Eugenics 7, Pt. II, 179-188. As found here](https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2)
2. [Abhishek Gupta's analysis of the Fisher Dataset on kaggle.com](https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation)
3. [An overview of the Iris Dataset from Codebag NG incl. some programs to help analyze it](https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)
4. [Edukast's Youtube video on Machine Learning Classification - specifically using Fisher's Iris Dataset](https://www.youtube.com/watch?v=wIubuU7gejM)
5. [Dr. Ian McLoughlin's GMIT lectures](https://web.microsoftstream.com/video/6db924ef-af13-47da-a620-0e5b59e1c0ff)
6. [Writing readme.md files on Github](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
7. [Creating tables in markdown](https://www.makeuseof.com/tag/create-markdown-table/)
