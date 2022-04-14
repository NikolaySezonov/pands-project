# PANDS project on Fisher's Iris Data set

# Part of the overall course of Diploma in Computing in Data Analytics

# Thsi program is intend to read an input from a csv file of the 'Fisher’s Iris data set', then the program analyses the iris data set, outputs a number of csv summary files
# and gives the user an option to create a number of different scatter plots.

# Author: Nikolay Sezonov

# Submission date 16-Apr-22 as I have to submitted earlier :)

# After conducting some research 4 modules that i most likely will use with this programme are as follows:
 
import matplotlib.pyplot as plt
import pandas as pd 

# import matplotlib pyplot and pandasmodules abbreviated to plt and pd

iris_data = pd.read_csv("Iris-data-set.csv", header=None) 

# here I am setting up a variable for use in the program

iris_data.columns =["Sepal length (cm)","Sepal width (cm)","Petal length (cm)","Petal width (cm)","Species"]
# Adding headers to attributes (columns); source: https://stackoverflow.com/a/28162530

print(iris_data.head())