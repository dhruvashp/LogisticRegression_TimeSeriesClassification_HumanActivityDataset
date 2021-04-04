# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 03:48:41 2020

@author: DHRUV
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


"""
We have a total of 18 features for our training set. Thus as the total plots are large rather
than going with the 18C2 approach and plotting separately, we'll directly obtain the 
18*18 scatter plot matrix using seaborn

Taking bending happens 1, otherwise 0, we obtain the following plots

"""

df = pd.read_csv('New_Train_Set.csv', index_col = 0)
print(df.head(15))

output = np.zeros(69)

one = np.arange(0,9)

i = 0
for i in one:
    output[i] = 1

df['Output'] = output

print(df.head(20))
print(df)


"""
We have only appended the output column here, to 1 where we have bending, and to 0 otherwise
"""


sns.pairplot(df, hue='Output')



