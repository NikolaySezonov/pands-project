# pands-project

### GMIT project for subject of Programming and Scripting 2022
### **********************************************************
### FAO: Mr. Andrew Beatty

Student Name        :      Nikolay Sezonov

Student ID          :      G00411604  

Submission Date     :      16 April 2022

GitHub              :      NikolaySezonov      


### The overall objective

The aim of this project is to indroduce the author to data research, code and analysis on very limited scale. The output will be based on example of Iris data set created by botanist Robert A.Fisher in 1936.

### Introduction

The data presented in this project has been investigated broadly and extensively across the globe, so there will be nothing new in it. The data set used in this project taken from "iris-data-set.csv" file. The name of the Python programme for this project is called "analyse.py". In order to run the code in the working folder ogf this project the following text should be used in the command line:

python analyse.py 

If the programme codes created/copied correctly by the author it should display some summaries of the data set content, output the summaries to csv files and will provide the options to user in plotting some of the figures.

### R.A Fisher and his iris flower data set

According to Britannica encyclopedia, Sir Ronald Aylmer Fisher, byname R.A. Fisher, (born February 17, 1890, London, England—died July 29, 1962, Adelaide, Australia) was a British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments. [1]

Fisher introduced the principle of randomization. This principle states that before an effect in an experiment can be ascribed to a given cause or treatment independently of other causes or treatments, the experiment must be repeated on a number of control units of the material and that all units of material used in the experiments must be randomly selected samples from the whole population they are intended to represent. [1]

Another important achievement by Fisher was origination of the concept of analysis of variance, or ANOVA, in which procedure enabled experiments may answer several questions at once. [1]

Back in 1936 the Iris flower set was introduced by Fisher. This flower data relates to the classification of three variant classes names of Iris flowers , namely:

1) Iris Versicolour 
2) Iris Setosa and
3) Iris Virginica

![ALT https://machinelearningsol.com/wp-content/uploads/2019/09/img1-1024x349.png ](https://machinelearningsol.com/wp-content/uploads/2019/09/img1-1024x349.png) [2]

and it contains fifty types of each of the three classes above, one hundred and fifty in total. [3]

There are five columns in this data set table and each column is an attribute of the each sample.
The first four attributes are the variations within each individual class, and the last attribute is the class itself. 

Those five attributes/columns names are as follows:

I)      Sepal length         represented in cm

II)     Sepal width          represented in cm

III)    Petal length         represented in cm

IV)     Petal width          represented in cm

V)      Class variant name

So, what is the difference between sepals and petals? 

Not sure if that's interesting, but still...

The sepals and petals together make up the perianth, or floral envelope. The sepals are usually greenish and often resemble reduced leaves, while the petals are usually colourful and showy to attract pollinators [4].

### Investigations on the Iris data set

One of the best advises I got from this course and from our lecturer Mr. Andrew Beatty is that project is just one module and it would not define me nor my life :) 

I knew from the very start, that I would really struggle with the whole coding thing, simply because it does takes time, dedication and commitment in learning something completely new. Saying that once you get to understand even a little bit as to how to "speak" with the programme in Python lingo, it will get just slightly easier.

Apologies, went off slightly from the topic... Ok, where are we? Oh, yes the investigations...

Different observations on-line shows [5] the data in Fisher's Iris data set [1] is good quality and what is most important is based on real life data. The quantity of data is large enough to work with.
It is also numerical, but is probably not enough to easily experimented with. But for teaching purposes is great.

During the copying of the data I noticed that the test print of the data showed 149 rows and that the first row of the data was used for the data header. 
I've changed that by running the following command and the issue was resolved

iris_data.columns =["Sepal length (cm)","Sepal width (cm)","Petal length (cm)","Petal width (cm)","Species"]

Then for the rest of the work I reviewed the key attributes of the data using the shape function. 
The output graphs from the program code can be found at the repository as the separate files.

1. Species Name:

Identification of the three types of Iris species within the dataset and 

2. Overview of key statistics of the Iris dataset:

This table displays the following analysis for all of the data entries combined:

Mean -              A measure of the centre for a distribution of a numeric variable. The total of all values divided by the total number of values

Count -             The total count of each value recorded. All counts are 150 representing a complete dataset and no null or void entries.

Standard deviation - A measure expressing the difference between numerical values and the mean of the category

Minimum, 25%, 50%, 75% maximum values - the corresponding values of each of the attributes in each column

Median: A measure of the centre for a distribution of a numeric variable. It splits the data in half with half the observations above and below.

Sample of Data contained in the Iris Dataset of all 150 records. The table aims to give a sample of the data not more than the 5 entries.

And finally.

Minimum, Maximum, Mean and Median of each attribute for each species in dataset. This is done for each of the attributes: sepal length, sepal width, petal length and petal width across all species.

All above are standard set of data investigations that I found across the web.

### Summary of findings of the Iris Data Set

The project tried to examined the key statistical attributes for the Iris flower dataset, namely the maximum, medium and standard deviation for all the data and also the individual species.

If these available, it would be great to explore any distinctions between attributes and species which could be used as a predictor indicators when you try to identify the different types of species.

To investigate this further, the max and min functions were used to identify the flowers associated with the data, allowing us to assume that sertosa type will be among the smallest data entries collected and virginica type will be among the largest data entries collected. 

It is well documented that the iris-sertosa and iris-virginica has more distinguishable attributes than the iris-versicolor [5].

The mean and median of the attributes are also important in exploing predictors as they were gathered as calculating the centre points. The central points for the sepal length and sepal width are less than 0.1, suggesting the mean and median are quite similiar.

The difference between the mean and median scores are more visible in the petal length and petal width, > 0.5. This may suggests that the data on petal lengths and petal widths could be used as an indication for the entry species.

To further visualise this data, the scatter plot " Corellation between Petal Length vs Petal Width & Sepal Length vs Sepal width" was created. This scatter plot demonstrates the spread of sepal sizes and petal sizes across the whole data set.

It is clear from the data set that there is a very high degree of correlation between the petal length and the petal width in the Iris species. Whereas in the sepal measurements there is no corellation observed at all and data is all over the place.

To me it's another proof that the nature is an absolute architect when it's come to proportions and measurements. That the reason why famous Antoni Gaudi always used nature in his work as he knew how to adapt the language of nature to the structural forms of architecture. 

Because petals are important when it comes to attract insects as a pollinators, it have to be in sertain proportions and colour so to be easility recognised / destinguished against other species.

I hope, that same as bee, I could collect enough of pollen = ["new knowledge"] to successfully transform and use it as a honey =["new skills"]  :)

### References

[1] https://www.britannica.com/biography/Ronald-Aylmer-Fisher

[2] https://machinelearningsol.com/wp-content/uploads/2019/09/img1-1024x349.png

[3] UC Irvine Machine Learning Repository. Iris data set. http://archive.ics.uci.edu/ml/datasets/Iris

[4] https://www.britannica.com/science/flower#ref49314

[5] https://stats.stackexchange.com/questions/74776/            what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching

[6] http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

### Links used and copied in the analyse.py program are from the following sources

* http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

* https://stackoverflow.com/a/28162530

* https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0

* https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.sample.html

* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html

* https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.plot.bar.html

* https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html

* https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib

* https://stackoverflow.com/questions/44383638/how-to-save-matplotlib-plot-with-the-same-file-name-as-its-filename-py

* http://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/

* https://seaborn.pydata.org/generated/seaborn.boxplot.html

* https://python-graph-gallery.com/30-basic-boxplot-with-seaborn/

* https://www.kaggle.com/sridharcr/data-analysis-iris-dataset

* https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation