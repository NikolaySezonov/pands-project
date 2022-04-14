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

print('Shape of the Iris Dataset')# Provides an overview of the data captured and potential outputs of further investigation Sourced: https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0

print(' ')

print(iris_data.shape) #Prints the number of data entries in the data set along with number of the attributes
#.shape is a module from the pandas package

