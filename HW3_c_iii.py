# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:11:55 2020

@author: DHRUV
"""


"""
HW3 (c) (iii)
"""

"""
Total 42 features, we need to find standard deviation of each feature. Also we haven't
standardized/normalized the data, we've just used the raw data.

"""

import pandas as pd
import numpy as np


features = pd.read_csv('Extracted_Whole_Feature.csv', index_col = 0)
print(features)
std_features = features.std(axis=0)
print('The standard deviation of all the features over the training and the test sets (all 88 instances) are : \n',std_features)

"""
This standard deviation is calculated with N-1 in the denominator as taken by pandas by
default

"""
headers = ['avg_rss12_mean', 'avg_rss12_std', 'avg_rss12_min', 'avg_rss12_q1','avg_rss12_median', 'avg_rss12_q3','avg_rss12_max','var_rss12_mean', 'var_rss12_std', 'var_rss12_min', 'var_rss12_q1','var_rss12_median', 'var_rss12_q3','var_rss12_max','avg_rss13_mean', 'avg_rss13_std', 'avg_rss13_min', 'avg_rss13_q1','avg_rss13_median', 'avg_rss13_q3','avg_rss13_max','var_rss13_mean', 'var_rss13_std', 'var_rss13_min', 'var_rss13_q1','var_rss13_median', 'var_rss13_q3','var_rss13_max','avg_rss23_mean', 'avg_rss23_std', 'avg_rss23_min', 'avg_rss23_q1','avg_rss23_median', 'avg_rss23_q3','avg_rss23_max','var_rss23_mean', 'var_rss23_std', 'var_rss23_min', 'var_rss23_q1','var_rss23_median', 'var_rss23_q3','var_rss23_max']
std_matrix = pd.DataFrame(index = range(0,100), columns = headers)
col = np.arange(0,42)
bootstrap = np.arange(0,100)
size = 88 

i = 0

for i in col:
    df = features.iloc[:,i]
    df_arr = df.to_numpy()
    df_flt = df_arr.flatten()
    
    j = 0
    
    for j in bootstrap:
        arr_interim = np.random.choice(df_flt, size = 88)
        std_matrix.iloc[j,i] = np.std(arr_interim, ddof = 1)
        
        

print('The bootstrap matrix of standard deviations obtained for each bootstrap sample for each feature is as follows : \n', std_matrix)

confidence_matrix = pd.DataFrame(index = headers, columns = ['start','end'])    

i=0
for i in col:
    df = std_matrix.iloc[:,i]
    df_arr = df.to_numpy()
    df_flt = df_arr.flatten()
    df_sort = np.sort(df_flt)
    confidence_matrix.iloc[i,0]=df_sort[5]
    confidence_matrix.iloc[i,1]=df_sort[94]
    


print('With confidence interval of 90%, the range of standard deviation obtained, empirically via bootstrap is as follows : \n', confidence_matrix)




"""

We've used np.random.choice here. Also we have obtained standard deviation of our entire
feature dataset not just the training or the test one. Since the question didn't clarify
which dataset, I've used the entire instances dataset of all 88 instances including the test
instances and the training instances

"""

    

