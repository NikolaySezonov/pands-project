# PANDS project on Fisher's Iris Data set

# Part of the overall course of Diploma in Computing in Data Analytics

# Thsi program is intend to read an input from a csv file of the 'Fisher’s Iris data set', then the program analyses the iris data set, outputs a number of csv summary files
# and gives the user an option to create a number of different scatter plots.

# Author: Nikolay Sezonov

# Submission date 16-Apr-22 as I have to submitted earlier :)

# After conducting some research 2 modules that i most likely will use with this programme are as follows:
 
import matplotlib.pyplot as plt
import pandas as pd 

# import matplotlib pyplot and pandasmodules abbreviated to plt and pd

iris_data = pd.read_csv("Iris-data-set.csv", header=None) 

# here I am setting up a variable for use in the program

iris_data.columns =["Sepal length (cm)","Sepal width (cm)","Petal length (cm)","Petal width (cm)","Species"]
# Adding headers to attributes (columns); source: https://stackoverflow.com/a/28162530



print(' ') #use of space to make the output more user friendly

print ("Investigations on Iris Dataset") #Title of program being run

print ("All Graphs within this program will be automatically saved in the folder for viewing")

print(' ')

print('Unique Species Names') # this programme is being run to allow the user to indentify the three types of iris flower in the dataset

print(' ')

print(iris_data['Species'].unique()) #prints out the three types of iris species captured

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')
# the above block is used as a spacing tool for ease of usability and readability for the users

print('Shape of the Iris Dataset')# Provides an overview of the data captured and potential outputs 
# of further investigation Sourced: https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0

print(' ')

print(iris_data.shape) #Prints the number of data entries in the data set along with number of the attributes
#.shape is a module from the pandas package

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Sample of Data contained in the Iris Dataset of all 150 records')# random sample of the dataset. 
# source: https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sample.html
print(' ')
print (iris_data.sample (5)) #Prints 5 random complete data entries from the data set
x = iris_data.sample(5)
#.sample is a module from the pandas package to enable to user to see a random seletion of data 
# from the dataset

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ("Summary of Key Statistics from Iris Dataset of all 150 records") 
# generates statistical analysis of the features of the measures of centre points and 
# distribution of values 
# source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
print(' ')
print (iris_data.describe()) 
# Prints in tabular form key statistics from the data.
# provide high level analysis for the user
#.describe - a module that outputs the key statistics of the dataset
# output sets the scene for following investigations that are more indepth and particular to each species
print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print('Median of attributes from Iris Dataset of all 150 records') 
# this is an additional analysis conducted on the centre points of the data 
# source: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html

print(' ')
print(iris_data.median()) # Print the median of each of the attributes in tabular form

print(' ')
print('------------------------------------------------------------------------------------------------------------')
print(' ')

print ('Minimum, Maximum, Mean and Median of each attribute for each species in dataset') #the following analysis looks at the maximum, minimum, mean and median of each of the numerical categories
print(' ')
#all modules are from the pandas package

print('Min ') 
# Extracts the minimum values of each of the attributes 
print(iris_data.groupby('Species').min()) # Prints in tabular form and also groups the data by the three species
#Graph variables set up for bar chart to be displayed and saved into the repository

iris_min = iris_data.groupby('Species').min()
iris_min.plot.bar() 
# Module to create table of minimum values for each species. 
# Source: https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.plot.bar.html

plt.gcf().subplots_adjust(bottom=0.15) 
# adjusting the table to enable table to be fully seen in the window. 
# Source: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html

plt.xlabel('Iris Species', fontsize=14, weight='normal')
# applying text and font to the table on the x axis. 
# Source: https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib

plt.ylabel("Min Values", fontsize=14, weight='normal')
# applying text and font to the table on the y axis

title = "Min Value of Attributes of each of Iris Species" 
# Applying a title to the dataset

filename = "Min Value of Attributes of each of Iris Species.jpg" 
# the name of the file to which the graph will be saved to

plt.title(title, fontsize=14, weight='bold') 
#apply text and font detail to the title

plt.gcf().subplots_adjust(bottom=0.3)
# plt.show()
# plt.close()

filename = "Min of Attributes of each of Iris Species.jpg"

plt.savefig(filename) 
# file will be saved and then will close to allow continuing of the program execution. 
# Source:https://stackoverflow.com/questions/44383638/how-to-save-matplotlib-plot-with-the-same-file-name-as-its-filename-py

plt.close()
print(' ')



print('Max')  # Extracts the maximum values of each of the attributes 
print(iris_data.groupby('Species').max()) 

# The sources and explaination are the same for all tables in this group

#Graph variables set up for bar chart to be displayed and saved into the repository

iris_max = iris_data.groupby('Species').max()
iris_max.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=14, weight='normal')
plt.ylabel("Max Values", fontsize=14, weight='normal')
title = "Max Value of Attributes of each of Iris Species"
plt.title(title, fontsize=14, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
#plt.show()
#plt.close()
filename = "Max of Attributes of each of Iris Species.jpg"
plt.savefig(filename)
plt.close()
print(' ')

print('Mean')  # Extracts the maximum values of each of the attributes 
print(iris_data.groupby('Species').mean()) # Prints in tabular form
print(' ')

#Graph variables set up for bar chart to be displayed and saved into the repository
iris_mean = iris_data.groupby('Species').mean()
iris_mean.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species', fontsize=14, weight='normal')
plt.ylabel("Mean Values", fontsize=14, weight='normal')
title = "Mean Value of Attributes of each of Iris Species"
filename = "Mean Value of Attributes of each of Iris Species.jpg"
plt.title(title, fontsize=14, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
#plt.show()
#plt.close()

filename = "Mean of Attributes in Iris dataset.jpg"
plt.savefig(filename)
plt.close()
print(' ')

print('Median')  # Extracts the median values of each of the attributes 
print(iris_data.groupby('Species').median()) # Prints in tabular form
print(' ')



#Graph variables set up for bar chart to be displayed and saved into the repository
iris_median = iris_data.groupby('Species').median()
iris_median.plot.bar()
plt.gcf().subplots_adjust(bottom=0.15)
plt.xlabel('Species',fontsize=14, weight='normal')
plt.ylabel("Median Values", fontsize=14, weight='normal')
title = "Median Value of Attributes of each of Iris Species"
filename = "Median Value of Attributes of each of Iris Species.jpg"
plt.title(title, fontsize=26, weight='bold')
plt.gcf().subplots_adjust(bottom=0.3)
#plt.show()
filename = "Median of Attributes of each of Iris Species.jpg"
plt.savefig(filename)
plt.close()
print(' ')

