# test file to create a summary of the dataset
# to be used as the first part of the other, larger program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


