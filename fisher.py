import pandas as pd
iris = pd.read_csv("fishers_iris_dataset.csv",delimiter = ',') 
print ("Summary of Fisher's Iris Dataset")
print ("")
print (iris.describe())
print ("")
print ("Mean : Split by Species of Iris")
print ("")
print (iris.groupby('species').mean())
print ("")
print ("Median : Split by Species of Iris")
print ("")
print (iris.groupby('species').median())
# print (iris[["species","petal_length","sepal_length"]])
# scatter plot matrix
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import itertools
