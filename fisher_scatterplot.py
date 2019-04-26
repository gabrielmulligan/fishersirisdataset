# Programming and Scripting Project 2019 : Gabriel Mulligan

# Designing a Python program to 
# a) output a statistical summary (mean,min,max,standard deviation) of the Iris Dataset and
# b) plot this data in a Scatterplot diagram.
 
# Firstly, import the Python libraries required to analyze the data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.tools.plotting import scatter_matrix

# read in the actual Iris dataset data, as gathered by Edgar Anderson/Ronald Fisher (1936). 
# This is stored as fishers_iris_dataset.csv in this working directory.
iris = pd.read_csv("fishers_iris_dataset.csv",delimiter = ',') 

# print a statistical summary by Species
# Firstly, define each species in the dataset i.e. how Python knows which of the three Iris varieties it is
setosa=iris[iris['species']=='setosa']
versicolor =iris[iris['species']=='versicolor']
virginica =iris[iris['species']=='virginica']

# print a statistical summary using the describe function
print ("")
print ("Summary Statistical Analysis - Iris Setosa")
print(setosa.describe())
print ("")
print ("Summary Statistical Analysis - Iris Versicolor")
print(versicolor.describe())
print ("")
print ("Summary Statistical Analysis - Iris Virginica")
print(virginica.describe())
print ("")

# Now, for each Species, output a scatterplot of the Petal and Sepal Length/Width
# specify that we are going to output a diagram using the figure function, and that there are two subplots (two diagrams)
# ax[0] and ax[1]
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(21, 10))

# specifying the data for diagram 1 [ax[0] - The Sepal Length and Width
# the x, y and label values represent the headings in the csv file above
# the kind reflects the type of graph, colour represents the colour of the dots in the scatter graph.
setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

# specifying the data for diagram 2 [ax[1] - the Petal Length and Width
setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')

# Set the title, X/Y Labels and Legend of each diagram 
ax[0].set(title='Sepal Comparison ', xlabel='Sepal Length (cm)', ylabel='Sepal Width (cm)')
ax[1].set(title='Petal Comparison',  xlabel='Petal Length (cm)', ylabel='Petal Width (cm)')

# I want to draw attention to specific distribution patterns in the Scatterplots so I use the annotate and arrowprops
# functions to point out the data that shows a specific pattern.
# the text is the text I want to output, the xy is the scatterpoint co-ordinates that I want to point the arrow to. 
# The xytext are the co-ordinates where I want to start printing the text.
plt.annotate('Satosa petals are smaller than other varieties so easier to segregate', xy=(1.6, 0.6), xytext=(1.7, 0.7),
        arrowprops=dict(arrowstyle="->", facecolor='red'),
        )
plt.annotate('Versicolor and Virginica are bunched closer together', xy=(4.5, 1.7), xytext=(1.0, 2.0),
        arrowprops=dict(arrowstyle="->", facecolor='green'),
        )
plt.annotate('so harder to seperate', xy=(4.5, 1.7), xytext=(1.0, 1.9))

# output the legend for each graphs
ax[0].legend()
ax[1].legend()

# output the graphs
plt.show()
plt.close()
