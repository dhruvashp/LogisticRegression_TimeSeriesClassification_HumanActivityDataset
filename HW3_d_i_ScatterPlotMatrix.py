# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 04:11:39 2020

@author: DHRUV
"""

"""
HW3_d_i_ScatterPlotMatrix

"""

"""
We obtained individual scatter plots in d_i
Now we obtain the scatterplot matrix as well to compare with scatterplot matrix in d_ii

NOTE : The train_bend has already been appended with 0/1 output in the .csv extracted
file itself

"""

import pandas as pd
import seaborn as sns


df = pd.read_csv('train_bend.csv', index_col = 0)
print(df)

sns.pairplot(df, hue = 'Output')

