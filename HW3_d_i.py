# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 08:59:14 2020

@author: DHRUV
"""


"""
HW3 (d) (i)

Few Comments -
We extracted all the instances and their features in an 88 x 42 matrix

We seperate the training and test instances now, in the following way -
For bending1 and bending2, dataset1 and dataset2 were test, the rest were train
For all the other activities, datasets 1,2,3 were test, rest were train

So we'll perform this modification in the Extracted excel file itself, rather
than perform it in Python as it's easier. 

Other than splitting instances into train and test, we also have to redact the feature column

As stated in the question, we'll use the first two and the last time series (1,2,6) and select
from each time series the feature of max, mean, standard deviation as selected in the previous question

Thus, we'll get total 3*3 = 9 features

Training set will have 69 instances, and test set will have 19 instances

Also as we want to classify, in a binary sense, bending from other activities, we'll append an
output column which will be -

1 if it corresponds to bending1 or bending2 instant
0 otherwise

Thus we'll perform all these changes in Excel as it is a small dataset, and the final excel .csv
files will be named -

train_bend
test_bend

train_bend will have 69 x 10 dimension
test_bend will have 19 x 10 dimension



"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


train_bend = pd.read_csv('train_bend.csv', index_col = 0)
test_bend = pd.read_csv('test_bend.csv', index_col = 0)

print(train_bend)
print(test_bend)

"""
Assumption for Scatter Plots -
We'll perform the scatter plots for only the training data, as that is the data the 
model will see, and should be the plots over which data should be observed

"""

sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,1], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,2], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,3], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,4], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,5], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,6], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,7], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,0], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()




sns.scatterplot(data=train_bend, x=train_bend.iloc[:,1], y=train_bend.iloc[:,2], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,1], y=train_bend.iloc[:,3], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,1], y=train_bend.iloc[:,4], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,1], y=train_bend.iloc[:,5], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,1], y=train_bend.iloc[:,6], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,1], y=train_bend.iloc[:,7], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,1], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()




sns.scatterplot(data=train_bend, x=train_bend.iloc[:,2], y=train_bend.iloc[:,3], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,2], y=train_bend.iloc[:,4], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,2], y=train_bend.iloc[:,5], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,2], y=train_bend.iloc[:,6], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,2], y=train_bend.iloc[:,7], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,2], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()





sns.scatterplot(data=train_bend, x=train_bend.iloc[:,3], y=train_bend.iloc[:,4], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,3], y=train_bend.iloc[:,5], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,3], y=train_bend.iloc[:,6], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,3], y=train_bend.iloc[:,7], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,3], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()


sns.scatterplot(data=train_bend, x=train_bend.iloc[:,4], y=train_bend.iloc[:,5], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,4], y=train_bend.iloc[:,6], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,4], y=train_bend.iloc[:,7], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,4], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()



sns.scatterplot(data=train_bend, x=train_bend.iloc[:,5], y=train_bend.iloc[:,6], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,5], y=train_bend.iloc[:,7], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,5], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()


sns.scatterplot(data=train_bend, x=train_bend.iloc[:,6], y=train_bend.iloc[:,7], hue = 'Output')
plt.show()
sns.scatterplot(data=train_bend, x=train_bend.iloc[:,6], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()


sns.scatterplot(data=train_bend, x=train_bend.iloc[:,7], y=train_bend.iloc[:,8], hue = 'Output')
plt.show()






"""
We have one feature on the x-axis and a different feature on the y-axis

Hue decided by the output

Thus all in all we have a total of 9C2 or 36 total curves

"""
