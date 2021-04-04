# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:09:31 2020

@author: DHRUV
"""


"""
HW3 (d) (ii)

"""

"""
Getting our training data -
We have been told here to work with training instances. Using the training instances for each 
activity, we have to perform the following -
We'll split the instances in half row-wise. This half will be appended to columns adjacent to our
6 time series in the same order. That is the second half of time series 1 in column 1 will be in the column
7 and so on and so forth

"""
"""
Also additional assumptions -
We have assumed the wording is incorrect. We'll take both parts of columns 1,2,6 split in half
So we'll take time series 1,2,6 both parts (so 6 effective time series) and three features from
each part, for a total of 18 features. And 69 training rows. So the feature matrix will be
69*18 

We'll also then append a final column corresponding to the output

"""
import pandas as pd
import numpy as np

b1_3 = pd.read_csv('bending1\\training\\dataset3.csv')
print(b1_3)
a_b1_3 = b1_3.iloc[0:240,1:]
b_b1_3 = b1_3.iloc[240:480,1:]
b_b1_3.reset_index(drop=True, inplace = True)
print(a_b1_3)
print(b_b1_3)
b1_3_f = a_b1_3.join(b_b1_3, lsuffix='_1', rsuffix='_2')
print(b1_3_f)





b1_4 = pd.read_csv('bending1\\training\\dataset4.csv')
print(b1_4)
a_b1_4 = b1_4.iloc[0:240,1:]
b_b1_4 = b1_4.iloc[240:480,1:]
b_b1_4.reset_index(drop=True, inplace = True)
print(a_b1_4)
print(b_b1_4)
b1_4_f = a_b1_4.join(b_b1_4, lsuffix='_1', rsuffix='_2')
print(b1_4_f)

b1_5 = pd.read_csv('bending1\\training\\dataset5.csv')
print(b1_5)
a_b1_5 = b1_5.iloc[0:240,1:]
b_b1_5 = b1_5.iloc[240:480,1:]
b_b1_5.reset_index(drop=True, inplace = True)
print(a_b1_5)
print(b_b1_5)
b1_5_f = a_b1_5.join(b_b1_5, lsuffix='_1', rsuffix='_2')
print(b1_5_f)

b1_6 = pd.read_csv('bending1\\training\\dataset6.csv')
print(b1_6)
a_b1_6 = b1_6.iloc[0:240,1:]
b_b1_6 = b1_6.iloc[240:480,1:]
b_b1_6.reset_index(drop=True, inplace = True)
print(a_b1_6)
print(b_b1_6)
b1_6_f = a_b1_6.join(b_b1_6, lsuffix='_1', rsuffix='_2')
print(b1_6_f)

b1_7 = pd.read_csv('bending1\\training\\dataset7.csv')
print(b1_7)
a_b1_7 = b1_7.iloc[0:240,1:]
b_b1_7 = b1_7.iloc[240:480,1:]
b_b1_7.reset_index(drop=True, inplace = True)
print(a_b1_7)
print(b_b1_7)
b1_7_f = a_b1_7.join(b_b1_7, lsuffix='_1', rsuffix='_2')
print(b1_7_f)










b2_3 = pd.read_csv('bending2\\training\\dataset3.csv')
print(b2_3)
a_b2_3 = b2_3.iloc[0:240,1:]
b_b2_3 = b2_3.iloc[240:480,1:]
b_b2_3.reset_index(drop=True, inplace = True)
print(a_b2_3)
print(b_b2_3)
b2_3_f = a_b2_3.join(b_b2_3, lsuffix='_1', rsuffix='_2')
print(b2_3_f)

b2_4 = pd.read_csv('bending2\\training\\dataset4.csv')
print(b2_4)
a_b2_4 = b2_4.iloc[0:240,1:]
b_b2_4 = b2_4.iloc[240:480,1:]
b_b2_4.reset_index(drop=True, inplace = True)
print(a_b2_4)
print(b_b2_4)
b2_4_f = a_b2_4.join(b_b2_4, lsuffix='_1', rsuffix='_2')
print(b2_4_f)


b2_5 = pd.read_csv('bending2\\training\\dataset5.csv')
print(b2_5)
a_b2_5 = b2_5.iloc[0:240,1:]
b_b2_5 = b2_5.iloc[240:480,1:]
b_b2_5.reset_index(drop=True, inplace = True)
print(a_b2_5)
print(b_b2_5)
b2_5_f = a_b2_5.join(b_b2_5, lsuffix='_1', rsuffix='_2')
print(b2_5_f)


b2_6 = pd.read_csv('bending2\\training\\dataset6.csv')
print(b2_6)
a_b2_6 = b2_6.iloc[0:240,1:]
b_b2_6 = b2_6.iloc[240:480,1:]
b_b2_6.reset_index(drop=True, inplace = True)
print(a_b2_6)
print(b_b2_6)
b2_6_f = a_b2_6.join(b_b2_6, lsuffix='_1', rsuffix='_2')
print(b2_6_f)

















cy_4 = pd.read_csv('cycling\\training\\dataset4.csv')
print(cy_4)
a_cy_4 = cy_4.iloc[0:240,1:]
b_cy_4 = cy_4.iloc[240:480,1:]
b_cy_4.reset_index(drop=True, inplace = True)
print(a_cy_4)
print(b_cy_4)
cy_4_f = a_cy_4.join(b_cy_4, lsuffix='_1', rsuffix='_2')
print(cy_4_f)


cy_5 = pd.read_csv('cycling\\training\\dataset5.csv')
print(cy_5)
a_cy_5 = cy_5.iloc[0:240,1:]
b_cy_5 = cy_5.iloc[240:480,1:]
b_cy_5.reset_index(drop=True, inplace = True)
print(a_cy_5)
print(b_cy_5)
cy_5_f = a_cy_5.join(b_cy_5, lsuffix='_1', rsuffix='_2')
print(cy_5_f)


cy_6 = pd.read_csv('cycling\\training\\dataset6.csv')
print(cy_6)
a_cy_6 = cy_6.iloc[0:240,1:]
b_cy_6 = cy_6.iloc[240:480,1:]
b_cy_6.reset_index(drop=True, inplace = True)
print(a_cy_6)
print(b_cy_6)
cy_6_f = a_cy_6.join(b_cy_6, lsuffix='_1', rsuffix='_2')
print(cy_6_f)


cy_7 = pd.read_csv('cycling\\training\\dataset7.csv')
print(cy_7)
a_cy_7 = cy_7.iloc[0:240,1:]
b_cy_7 = cy_7.iloc[240:480,1:]
b_cy_7.reset_index(drop=True, inplace = True)
print(a_cy_7)
print(b_cy_7)
cy_7_f = a_cy_7.join(b_cy_7, lsuffix='_1', rsuffix='_2')
print(cy_7_f)


cy_8 = pd.read_csv('cycling\\training\\dataset8.csv')
print(cy_8)
a_cy_8 = cy_8.iloc[0:240,1:]
b_cy_8 = cy_8.iloc[240:480,1:]
b_cy_8.reset_index(drop=True, inplace = True)
print(a_cy_8)
print(b_cy_8)
cy_8_f = a_cy_8.join(b_cy_8, lsuffix='_1', rsuffix='_2')
print(cy_8_f)

cy_9 = pd.read_csv('cycling\\training\\dataset9.csv')
print(cy_9)
a_cy_9 = cy_9.iloc[0:240,1:]
b_cy_9 = cy_9.iloc[240:480,1:]
b_cy_9.reset_index(drop=True, inplace = True)
print(a_cy_9)
print(b_cy_9)
cy_9_f = a_cy_9.join(b_cy_9, lsuffix='_1', rsuffix='_2')
print(cy_9_f)


cy_10 = pd.read_csv('cycling\\training\\dataset10.csv')
print(cy_10)
a_cy_10 = cy_10.iloc[0:240,1:]
b_cy_10 = cy_10.iloc[240:480,1:]
b_cy_10.reset_index(drop=True, inplace = True)
print(a_cy_10)
print(b_cy_10)
cy_10_f = a_cy_10.join(b_cy_10, lsuffix='_1', rsuffix='_2')
print(cy_10_f)


cy_11 = pd.read_csv('cycling\\training\\dataset11.csv')
print(cy_11)
a_cy_11 = cy_11.iloc[0:240,1:]
b_cy_11 = cy_11.iloc[240:480,1:]
b_cy_11.reset_index(drop=True, inplace = True)
print(a_cy_11)
print(b_cy_11)
cy_11_f = a_cy_11.join(b_cy_11, lsuffix='_1', rsuffix='_2')
print(cy_11_f)


cy_12 = pd.read_csv('cycling\\training\\dataset12.csv')
print(cy_12)
a_cy_12 = cy_12.iloc[0:240,1:]
b_cy_12 = cy_12.iloc[240:480,1:]
b_cy_12.reset_index(drop=True, inplace = True)
print(a_cy_12)
print(b_cy_12)
cy_12_f = a_cy_12.join(b_cy_12, lsuffix='_1', rsuffix='_2')
print(cy_12_f)


cy_13 = pd.read_csv('cycling\\training\\dataset13.csv')
print(cy_13)
a_cy_13 = cy_13.iloc[0:240,1:]
b_cy_13 = cy_13.iloc[240:480,1:]
b_cy_13.reset_index(drop=True, inplace = True)
print(a_cy_13)
print(b_cy_13)
cy_13_f = a_cy_13.join(b_cy_13, lsuffix='_1', rsuffix='_2')
print(cy_13_f)


cy_14 = pd.read_csv('cycling\\training\\dataset14.csv')
print(cy_14)
a_cy_14 = cy_14.iloc[0:240,1:]
b_cy_14 = cy_14.iloc[240:480,1:]
b_cy_14.reset_index(drop=True, inplace = True)
print(a_cy_14)
print(b_cy_14)
cy_14_f = a_cy_14.join(b_cy_14, lsuffix='_1', rsuffix='_2')
print(cy_14_f)


cy_15 = pd.read_csv('cycling\\training\\dataset15.csv')
print(cy_15)
a_cy_15 = cy_15.iloc[0:240,1:]
b_cy_15 = cy_15.iloc[240:480,1:]
b_cy_15.reset_index(drop=True, inplace = True)
print(a_cy_15)
print(b_cy_15)
cy_15_f = a_cy_15.join(b_cy_15, lsuffix='_1', rsuffix='_2')
print(cy_15_f)




















ly_4 = pd.read_csv('lying\\training\\dataset4.csv')
print(ly_4)
a_ly_4 = ly_4.iloc[0:240,1:]
b_ly_4 = ly_4.iloc[240:480,1:]
b_ly_4.reset_index(drop=True, inplace = True)
print(a_ly_4)
print(b_ly_4)
ly_4_f = a_ly_4.join(b_ly_4, lsuffix='_1', rsuffix='_2')
print(ly_4_f)


ly_5 = pd.read_csv('lying\\training\\dataset5.csv')
print(ly_5)
a_ly_5 = ly_5.iloc[0:240,1:]
b_ly_5 = ly_5.iloc[240:480,1:]
b_ly_5.reset_index(drop=True, inplace = True)
print(a_ly_5)
print(b_ly_5)
ly_5_f = a_ly_5.join(b_ly_5, lsuffix='_1', rsuffix='_2')
print(ly_5_f)


ly_6 = pd.read_csv('lying\\training\\dataset6.csv')
print(ly_6)
a_ly_6 = ly_6.iloc[0:240,1:]
b_ly_6 = ly_6.iloc[240:480,1:]
b_ly_6.reset_index(drop=True, inplace = True)
print(a_ly_6)
print(b_ly_6)
ly_6_f = a_ly_6.join(b_ly_6, lsuffix='_1', rsuffix='_2')
print(ly_6_f)


ly_7 = pd.read_csv('lying\\training\\dataset7.csv')
print(ly_7)
a_ly_7 = ly_7.iloc[0:240,1:]
b_ly_7 = ly_7.iloc[240:480,1:]
b_ly_7.reset_index(drop=True, inplace = True)
print(a_ly_7)
print(b_ly_7)
ly_7_f = a_ly_7.join(b_ly_7, lsuffix='_1', rsuffix='_2')
print(ly_7_f)


ly_8 = pd.read_csv('lying\\training\\dataset8.csv')
print(ly_8)
a_ly_8 = ly_8.iloc[0:240,1:]
b_ly_8 = ly_8.iloc[240:480,1:]
b_ly_8.reset_index(drop=True, inplace = True)
print(a_ly_8)
print(b_ly_8)
ly_8_f = a_ly_8.join(b_ly_8, lsuffix='_1', rsuffix='_2')
print(ly_8_f)

ly_9 = pd.read_csv('lying\\training\\dataset9.csv')
print(ly_9)
a_ly_9 = ly_9.iloc[0:240,1:]
b_ly_9 = ly_9.iloc[240:480,1:]
b_ly_9.reset_index(drop=True, inplace = True)
print(a_ly_9)
print(b_ly_9)
ly_9_f = a_ly_9.join(b_ly_9, lsuffix='_1', rsuffix='_2')
print(ly_9_f)


ly_10 = pd.read_csv('lying\\training\\dataset10.csv')
print(ly_10)
a_ly_10 = ly_10.iloc[0:240,1:]
b_ly_10 = ly_10.iloc[240:480,1:]
b_ly_10.reset_index(drop=True, inplace = True)
print(a_ly_10)
print(b_ly_10)
ly_10_f = a_ly_10.join(b_ly_10, lsuffix='_1', rsuffix='_2')
print(ly_10_f)


ly_11 = pd.read_csv('lying\\training\\dataset11.csv')
print(ly_11)
a_ly_11 = ly_11.iloc[0:240,1:]
b_ly_11 = ly_11.iloc[240:480,1:]
b_ly_11.reset_index(drop=True, inplace = True)
print(a_ly_11)
print(b_ly_11)
ly_11_f = a_ly_11.join(b_ly_11, lsuffix='_1', rsuffix='_2')
print(ly_11_f)


ly_12 = pd.read_csv('lying\\training\\dataset12.csv')
print(ly_12)
a_ly_12 = ly_12.iloc[0:240,1:]
b_ly_12 = ly_12.iloc[240:480,1:]
b_ly_12.reset_index(drop=True, inplace = True)
print(a_ly_12)
print(b_ly_12)
ly_12_f = a_ly_12.join(b_ly_12, lsuffix='_1', rsuffix='_2')
print(ly_12_f)


ly_13 = pd.read_csv('lying\\training\\dataset13.csv')
print(ly_13)
a_ly_13 = ly_13.iloc[0:240,1:]
b_ly_13 = ly_13.iloc[240:480,1:]
b_ly_13.reset_index(drop=True, inplace = True)
print(a_ly_13)
print(b_ly_13)
ly_13_f = a_ly_13.join(b_ly_13, lsuffix='_1', rsuffix='_2')
print(ly_13_f)


ly_14 = pd.read_csv('lying\\training\\dataset14.csv')
print(ly_14)
a_ly_14 = ly_14.iloc[0:240,1:]
b_ly_14 = ly_14.iloc[240:480,1:]
b_ly_14.reset_index(drop=True, inplace = True)
print(a_ly_14)
print(b_ly_14)
ly_14_f = a_ly_14.join(b_ly_14, lsuffix='_1', rsuffix='_2')
print(ly_14_f)


ly_15 = pd.read_csv('lying\\training\\dataset15.csv')
print(ly_15)
a_ly_15 = ly_15.iloc[0:240,1:]
b_ly_15 = ly_15.iloc[240:480,1:]
b_ly_15.reset_index(drop=True, inplace = True)
print(a_ly_15)
print(b_ly_15)
ly_15_f = a_ly_15.join(b_ly_15, lsuffix='_1', rsuffix='_2')
print(ly_15_f)





























sit_4 = pd.read_csv('sitting\\training\\dataset4.csv')
print(sit_4)
a_sit_4 = sit_4.iloc[0:240,1:]
b_sit_4 = sit_4.iloc[240:480,1:]
b_sit_4.reset_index(drop=True, inplace = True)
print(a_sit_4)
print(b_sit_4)
sit_4_f = a_sit_4.join(b_sit_4, lsuffix='_1', rsuffix='_2')
print(sit_4_f)


sit_5 = pd.read_csv('sitting\\training\\dataset5.csv')
print(sit_5)
a_sit_5 = sit_5.iloc[0:240,1:]
b_sit_5 = sit_5.iloc[240:480,1:]
b_sit_5.reset_index(drop=True, inplace = True)
print(a_sit_5)
print(b_sit_5)
sit_5_f = a_sit_5.join(b_sit_5, lsuffix='_1', rsuffix='_2')
print(sit_5_f)


sit_6 = pd.read_csv('sitting\\training\\dataset6.csv')
print(sit_6)
a_sit_6 = sit_6.iloc[0:240,1:]
b_sit_6 = sit_6.iloc[240:480,1:]
b_sit_6.reset_index(drop=True, inplace = True)
print(a_sit_6)
print(b_sit_6)
sit_6_f = a_sit_6.join(b_sit_6, lsuffix='_1', rsuffix='_2')
print(sit_6_f)


sit_7 = pd.read_csv('sitting\\training\\dataset7.csv')
print(sit_7)
a_sit_7 = sit_7.iloc[0:240,1:]
b_sit_7 = sit_7.iloc[240:480,1:]
b_sit_7.reset_index(drop=True, inplace = True)
print(a_sit_7)
print(b_sit_7)
sit_7_f = a_sit_7.join(b_sit_7, lsuffix='_1', rsuffix='_2')
print(sit_7_f)


sit_8 = pd.read_csv('sitting\\training\\dataset8.csv')
print(sit_8)
a_sit_8 = sit_8.iloc[0:240,1:]
b_sit_8 = sit_8.iloc[240:480,1:]
b_sit_8.reset_index(drop=True, inplace = True)
print(a_sit_8)
print(b_sit_8)
sit_8_f = a_sit_8.join(b_sit_8, lsuffix='_1', rsuffix='_2')
print(sit_8_f)

sit_9 = pd.read_csv('sitting\\training\\dataset9.csv')
print(sit_9)
a_sit_9 = sit_9.iloc[0:240,1:]
b_sit_9 = sit_9.iloc[240:480,1:]
b_sit_9.reset_index(drop=True, inplace = True)
print(a_sit_9)
print(b_sit_9)
sit_9_f = a_sit_9.join(b_sit_9, lsuffix='_1', rsuffix='_2')
print(sit_9_f)


sit_10 = pd.read_csv('sitting\\training\\dataset10.csv')
print(sit_10)
a_sit_10 = sit_10.iloc[0:240,1:]
b_sit_10 = sit_10.iloc[240:480,1:]
b_sit_10.reset_index(drop=True, inplace = True)
print(a_sit_10)
print(b_sit_10)
sit_10_f = a_sit_10.join(b_sit_10, lsuffix='_1', rsuffix='_2')
print(sit_10_f)


sit_11 = pd.read_csv('sitting\\training\\dataset11.csv')
print(sit_11)
a_sit_11 = sit_11.iloc[0:240,1:]
b_sit_11 = sit_11.iloc[240:480,1:]
b_sit_11.reset_index(drop=True, inplace = True)
print(a_sit_11)
print(b_sit_11)
sit_11_f = a_sit_11.join(b_sit_11, lsuffix='_1', rsuffix='_2')
print(sit_11_f)


sit_12 = pd.read_csv('sitting\\training\\dataset12.csv')
print(sit_12)
a_sit_12 = sit_12.iloc[0:240,1:]
b_sit_12 = sit_12.iloc[240:480,1:]
b_sit_12.reset_index(drop=True, inplace = True)
print(a_sit_12)
print(b_sit_12)
sit_12_f = a_sit_12.join(b_sit_12, lsuffix='_1', rsuffix='_2')
print(sit_12_f)


sit_13 = pd.read_csv('sitting\\training\\dataset13.csv')
print(sit_13)
a_sit_13 = sit_13.iloc[0:240,1:]
b_sit_13 = sit_13.iloc[240:480,1:]
b_sit_13.reset_index(drop=True, inplace = True)
print(a_sit_13)
print(b_sit_13)
sit_13_f = a_sit_13.join(b_sit_13, lsuffix='_1', rsuffix='_2')
print(sit_13_f)


sit_14 = pd.read_csv('sitting\\training\\dataset14.csv')
print(sit_14)
a_sit_14 = sit_14.iloc[0:240,1:]
b_sit_14 = sit_14.iloc[240:480,1:]
b_sit_14.reset_index(drop=True, inplace = True)
print(a_sit_14)
print(b_sit_14)
sit_14_f = a_sit_14.join(b_sit_14, lsuffix='_1', rsuffix='_2')
print(sit_14_f)


sit_15 = pd.read_csv('sitting\\training\\dataset15.csv')
print(sit_15)
a_sit_15 = sit_15.iloc[0:240,1:]
b_sit_15 = sit_15.iloc[240:480,1:]
b_sit_15.reset_index(drop=True, inplace = True)
print(a_sit_15)
print(b_sit_15)
sit_15_f = a_sit_15.join(b_sit_15, lsuffix='_1', rsuffix='_2')
print(sit_15_f)





















stand_4 = pd.read_csv('standing\\training\\dataset4.csv')
print(stand_4)
a_stand_4 = stand_4.iloc[0:240,1:]
b_stand_4 = stand_4.iloc[240:480,1:]
b_stand_4.reset_index(drop=True, inplace = True)
print(a_stand_4)
print(b_stand_4)
stand_4_f = a_stand_4.join(b_stand_4, lsuffix='_1', rsuffix='_2')
print(stand_4_f)


stand_5 = pd.read_csv('standing\\training\\dataset5.csv')
print(stand_5)
a_stand_5 = stand_5.iloc[0:240,1:]
b_stand_5 = stand_5.iloc[240:480,1:]
b_stand_5.reset_index(drop=True, inplace = True)
print(a_stand_5)
print(b_stand_5)
stand_5_f = a_stand_5.join(b_stand_5, lsuffix='_1', rsuffix='_2')
print(stand_5_f)


stand_6 = pd.read_csv('standing\\training\\dataset6.csv')
print(stand_6)
a_stand_6 = stand_6.iloc[0:240,1:]
b_stand_6 = stand_6.iloc[240:480,1:]
b_stand_6.reset_index(drop=True, inplace = True)
print(a_stand_6)
print(b_stand_6)
stand_6_f = a_stand_6.join(b_stand_6, lsuffix='_1', rsuffix='_2')
print(stand_6_f)


stand_7 = pd.read_csv('standing\\training\\dataset7.csv')
print(stand_7)
a_stand_7 = stand_7.iloc[0:240,1:]
b_stand_7 = stand_7.iloc[240:480,1:]
b_stand_7.reset_index(drop=True, inplace = True)
print(a_stand_7)
print(b_stand_7)
stand_7_f = a_stand_7.join(b_stand_7, lsuffix='_1', rsuffix='_2')
print(stand_7_f)


stand_8 = pd.read_csv('standing\\training\\dataset8.csv')
print(stand_8)
a_stand_8 = stand_8.iloc[0:240,1:]
b_stand_8 = stand_8.iloc[240:480,1:]
b_stand_8.reset_index(drop=True, inplace = True)
print(a_stand_8)
print(b_stand_8)
stand_8_f = a_stand_8.join(b_stand_8, lsuffix='_1', rsuffix='_2')
print(stand_8_f)

stand_9 = pd.read_csv('standing\\training\\dataset9.csv')
print(stand_9)
a_stand_9 = stand_9.iloc[0:240,1:]
b_stand_9 = stand_9.iloc[240:480,1:]
b_stand_9.reset_index(drop=True, inplace = True)
print(a_stand_9)
print(b_stand_9)
stand_9_f = a_stand_9.join(b_stand_9, lsuffix='_1', rsuffix='_2')
print(stand_9_f)


stand_10 = pd.read_csv('standing\\training\\dataset10.csv')
print(stand_10)
a_stand_10 = stand_10.iloc[0:240,1:]
b_stand_10 = stand_10.iloc[240:480,1:]
b_stand_10.reset_index(drop=True, inplace = True)
print(a_stand_10)
print(b_stand_10)
stand_10_f = a_stand_10.join(b_stand_10, lsuffix='_1', rsuffix='_2')
print(stand_10_f)


stand_11 = pd.read_csv('standing\\training\\dataset11.csv')
print(stand_11)
a_stand_11 = stand_11.iloc[0:240,1:]
b_stand_11 = stand_11.iloc[240:480,1:]
b_stand_11.reset_index(drop=True, inplace = True)
print(a_stand_11)
print(b_stand_11)
stand_11_f = a_stand_11.join(b_stand_11, lsuffix='_1', rsuffix='_2')
print(stand_11_f)


stand_12 = pd.read_csv('standing\\training\\dataset12.csv')
print(stand_12)
a_stand_12 = stand_12.iloc[0:240,1:]
b_stand_12 = stand_12.iloc[240:480,1:]
b_stand_12.reset_index(drop=True, inplace = True)
print(a_stand_12)
print(b_stand_12)
stand_12_f = a_stand_12.join(b_stand_12, lsuffix='_1', rsuffix='_2')
print(stand_12_f)


stand_13 = pd.read_csv('standing\\training\\dataset13.csv')
print(stand_13)
a_stand_13 = stand_13.iloc[0:240,1:]
b_stand_13 = stand_13.iloc[240:480,1:]
b_stand_13.reset_index(drop=True, inplace = True)
print(a_stand_13)
print(b_stand_13)
stand_13_f = a_stand_13.join(b_stand_13, lsuffix='_1', rsuffix='_2')
print(stand_13_f)


stand_14 = pd.read_csv('standing\\training\\dataset14.csv')
print(stand_14)
a_stand_14 = stand_14.iloc[0:240,1:]
b_stand_14 = stand_14.iloc[240:480,1:]
b_stand_14.reset_index(drop=True, inplace = True)
print(a_stand_14)
print(b_stand_14)
stand_14_f = a_stand_14.join(b_stand_14, lsuffix='_1', rsuffix='_2')
print(stand_14_f)


stand_15 = pd.read_csv('standing\\training\\dataset15.csv')
print(stand_15)
a_stand_15 = stand_15.iloc[0:240,1:]
b_stand_15 = stand_15.iloc[240:480,1:]
b_stand_15.reset_index(drop=True, inplace = True)
print(a_stand_15)
print(b_stand_15)
stand_15_f = a_stand_15.join(b_stand_15, lsuffix='_1', rsuffix='_2')
print(stand_15_f)





















wa_4 = pd.read_csv('walking\\training\\dataset4.csv')
print(wa_4)
a_wa_4 = wa_4.iloc[0:240,1:]
b_wa_4 = wa_4.iloc[240:480,1:]
b_wa_4.reset_index(drop=True, inplace = True)
print(a_wa_4)
print(b_wa_4)
wa_4_f = a_wa_4.join(b_wa_4, lsuffix='_1', rsuffix='_2')
print(wa_4_f)


wa_5 = pd.read_csv('walking\\training\\dataset5.csv')
print(wa_5)
a_wa_5 = wa_5.iloc[0:240,1:]
b_wa_5 = wa_5.iloc[240:480,1:]
b_wa_5.reset_index(drop=True, inplace = True)
print(a_wa_5)
print(b_wa_5)
wa_5_f = a_wa_5.join(b_wa_5, lsuffix='_1', rsuffix='_2')
print(wa_5_f)


wa_6 = pd.read_csv('walking\\training\\dataset6.csv')
print(wa_6)
a_wa_6 = wa_6.iloc[0:240,1:]
b_wa_6 = wa_6.iloc[240:480,1:]
b_wa_6.reset_index(drop=True, inplace = True)
print(a_wa_6)
print(b_wa_6)
wa_6_f = a_wa_6.join(b_wa_6, lsuffix='_1', rsuffix='_2')
print(wa_6_f)


wa_7 = pd.read_csv('walking\\training\\dataset7.csv')
print(wa_7)
a_wa_7 = wa_7.iloc[0:240,1:]
b_wa_7 = wa_7.iloc[240:480,1:]
b_wa_7.reset_index(drop=True, inplace = True)
print(a_wa_7)
print(b_wa_7)
wa_7_f = a_wa_7.join(b_wa_7, lsuffix='_1', rsuffix='_2')
print(wa_7_f)


wa_8 = pd.read_csv('walking\\training\\dataset8.csv')
print(wa_8)
a_wa_8 = wa_8.iloc[0:240,1:]
b_wa_8 = wa_8.iloc[240:480,1:]
b_wa_8.reset_index(drop=True, inplace = True)
print(a_wa_8)
print(b_wa_8)
wa_8_f = a_wa_8.join(b_wa_8, lsuffix='_1', rsuffix='_2')
print(wa_8_f)

wa_9 = pd.read_csv('walking\\training\\dataset9.csv')
print(wa_9)
a_wa_9 = wa_9.iloc[0:240,1:]
b_wa_9 = wa_9.iloc[240:480,1:]
b_wa_9.reset_index(drop=True, inplace = True)
print(a_wa_9)
print(b_wa_9)
wa_9_f = a_wa_9.join(b_wa_9, lsuffix='_1', rsuffix='_2')
print(wa_9_f)


wa_10 = pd.read_csv('walking\\training\\dataset10.csv')
print(wa_10)
a_wa_10 = wa_10.iloc[0:240,1:]
b_wa_10 = wa_10.iloc[240:480,1:]
b_wa_10.reset_index(drop=True, inplace = True)
print(a_wa_10)
print(b_wa_10)
wa_10_f = a_wa_10.join(b_wa_10, lsuffix='_1', rsuffix='_2')
print(wa_10_f)


wa_11 = pd.read_csv('walking\\training\\dataset11.csv')
print(wa_11)
a_wa_11 = wa_11.iloc[0:240,1:]
b_wa_11 = wa_11.iloc[240:480,1:]
b_wa_11.reset_index(drop=True, inplace = True)
print(a_wa_11)
print(b_wa_11)
wa_11_f = a_wa_11.join(b_wa_11, lsuffix='_1', rsuffix='_2')
print(wa_11_f)


wa_12 = pd.read_csv('walking\\training\\dataset12.csv')
print(wa_12)
a_wa_12 = wa_12.iloc[0:240,1:]
b_wa_12 = wa_12.iloc[240:480,1:]
b_wa_12.reset_index(drop=True, inplace = True)
print(a_wa_12)
print(b_wa_12)
wa_12_f = a_wa_12.join(b_wa_12, lsuffix='_1', rsuffix='_2')
print(wa_12_f)


wa_13 = pd.read_csv('walking\\training\\dataset13.csv')
print(wa_13)
a_wa_13 = wa_13.iloc[0:240,1:]
b_wa_13 = wa_13.iloc[240:480,1:]
b_wa_13.reset_index(drop=True, inplace = True)
print(a_wa_13)
print(b_wa_13)
wa_13_f = a_wa_13.join(b_wa_13, lsuffix='_1', rsuffix='_2')
print(wa_13_f)


wa_14 = pd.read_csv('walking\\training\\dataset14.csv')
print(wa_14)
a_wa_14 = wa_14.iloc[0:240,1:]
b_wa_14 = wa_14.iloc[240:480,1:]
b_wa_14.reset_index(drop=True, inplace = True)
print(a_wa_14)
print(b_wa_14)
wa_14_f = a_wa_14.join(b_wa_14, lsuffix='_1', rsuffix='_2')
print(wa_14_f)


wa_15 = pd.read_csv('walking\\training\\dataset15.csv')
print(wa_15)
a_wa_15 = wa_15.iloc[0:240,1:]
b_wa_15 = wa_15.iloc[240:480,1:]
b_wa_15.reset_index(drop=True, inplace = True)
print(a_wa_15)
print(b_wa_15)
wa_15_f = a_wa_15.join(b_wa_15, lsuffix='_1', rsuffix='_2')
print(wa_15_f)


"""
The training instances have been obtained. The headers _1 and _2 represent the splitted
columns

Next we copy relevant features to the final training dataset

"""

col = np.arange(0,18)
indices = ['b1_3','b1_4','b1_5','b1_6','b1_7','b2_3','b2_4','b2_5','b2_6','cy_4','cy_5','cy_6','cy_7','cy_8','cy_9','cy_10','cy_11','cy_12','cy_13','cy_14','cy_15','ly_4','ly_5','ly_6','ly_7','ly_8','ly_9','ly_10','ly_11','ly_12','ly_13','ly_14','ly_15','sit_4','sit_5','sit_6','sit_7','sit_8','sit_9','sit_10','sit_11','sit_12','sit_13','sit_14','sit_15','stand_4','stand_5','stand_6','stand_7','stand_8','stand_9','stand_10','stand_11','stand_12','stand_13','stand_14','stand_15','wa_4','wa_5','wa_6','wa_7','wa_8','wa_9','wa_10','wa_11','wa_12','wa_13','wa_14','wa_15'] 
header = ['avg_rss12_1_mean','avg_rss12_1_std','avg_rss12_1_max','var_rss12_1_mean','var_rss12_1_std','var_rss12_1_max','var_rss23_1_mean','var_rss23_1_std','var_rss23_1_max','avg_rss12_2_mean','avg_rss12_2_std','avg_rss12_2_max','var_rss12_2_mean','var_rss12_2_std','var_rss12_2_max','var_rss23_2_mean','var_rss23_2_std','var_rss23_2_max']
new_train = pd.DataFrame(data=None, index = indices, columns = header)
print(new_train)


d_b1_3_f = b1_3_f.describe()
print(d_b1_3_f)

i=0



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b1_3_f.iloc[p,q]
        

print(new_train)




d_b1_4_f = b1_4_f.describe()
print(d_b1_4_f)

i=1



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b1_4_f.iloc[p,q]
        

print(new_train)









d_b1_5_f = b1_5_f.describe()
print(d_b1_5_f)

i=2



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b1_5_f.iloc[p,q]
        

print(new_train)








d_b1_6_f = b1_6_f.describe()
print(d_b1_6_f)

i=3



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b1_6_f.iloc[p,q]
        

print(new_train)






d_b1_7_f = b1_7_f.describe()
print(d_b1_7_f)

i=4



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b1_7_f.iloc[p,q]
        

print(new_train)



























d_b2_3_f = b2_3_f.describe()
print(d_b2_3_f)

i=5



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b2_3_f.iloc[p,q]
        

print(new_train)




d_b2_4_f = b2_4_f.describe()
print(d_b2_4_f)

i=6



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b2_4_f.iloc[p,q]
        

print(new_train)









d_b2_5_f = b2_5_f.describe()
print(d_b2_5_f)

i=7



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b2_5_f.iloc[p,q]
        

print(new_train)








d_b2_6_f = b2_6_f.describe()
print(d_b2_6_f)

i=8



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_b2_6_f.iloc[p,q]
        

print(new_train)























d_cy_4_f = cy_4_f.describe()
print(d_cy_4_f)

i=9



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_4_f.iloc[p,q]
        

print(new_train)












d_cy_5_f = cy_5_f.describe()
print(d_cy_5_f)

i=10



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_5_f.iloc[p,q]
        

print(new_train)


















d_cy_6_f = cy_6_f.describe()
print(d_cy_6_f)

i=11



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_6_f.iloc[p,q]
        

print(new_train)



















d_cy_7_f = cy_7_f.describe()
print(d_cy_7_f)

i=12



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_7_f.iloc[p,q]
        

print(new_train)
















d_cy_8_f = cy_8_f.describe()
print(d_cy_8_f)

i=13



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_8_f.iloc[p,q]
        

print(new_train)










d_cy_9_f = cy_9_f.describe()
print(d_cy_9_f)

i=14



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_9_f.iloc[p,q]
        

print(new_train)











d_cy_10_f = cy_10_f.describe()
print(d_cy_10_f)

i=15



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_10_f.iloc[p,q]
        

print(new_train)











d_cy_11_f = cy_11_f.describe()
print(d_cy_11_f)

i=16



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_11_f.iloc[p,q]
        

print(new_train)












d_cy_12_f = cy_12_f.describe()
print(d_cy_12_f)

i=17



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_12_f.iloc[p,q]
        

print(new_train)












d_cy_13_f = cy_13_f.describe()
print(d_cy_13_f)

i=18



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_13_f.iloc[p,q]
        

print(new_train)










d_cy_14_f = cy_14_f.describe()
print(d_cy_14_f)

i=19



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_14_f.iloc[p,q]
        

print(new_train)












d_cy_15_f = cy_15_f.describe()
print(d_cy_15_f)

i=20



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_cy_15_f.iloc[p,q]
        

print(new_train)






































d_ly_4_f = ly_4_f.describe()
print(d_ly_4_f)

i=21



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_4_f.iloc[p,q]
        

print(new_train)












d_ly_5_f = ly_5_f.describe()
print(d_ly_5_f)

i=22



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_5_f.iloc[p,q]
        

print(new_train)


















d_ly_6_f = ly_6_f.describe()
print(d_ly_6_f)

i=23



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_6_f.iloc[p,q]
        

print(new_train)



















d_ly_7_f = ly_7_f.describe()
print(d_ly_7_f)

i=24



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_7_f.iloc[p,q]
        

print(new_train)
















d_ly_8_f = ly_8_f.describe()
print(d_ly_8_f)

i=25



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_8_f.iloc[p,q]
        

print(new_train)










d_ly_9_f = ly_9_f.describe()
print(d_ly_9_f)

i=26



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_9_f.iloc[p,q]
        

print(new_train)











d_ly_10_f = ly_10_f.describe()
print(d_ly_10_f)

i=27



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_10_f.iloc[p,q]
        

print(new_train)











d_ly_11_f = ly_11_f.describe()
print(d_ly_11_f)

i=28



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_11_f.iloc[p,q]
        

print(new_train)












d_ly_12_f = ly_12_f.describe()
print(d_ly_12_f)

i=29



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_12_f.iloc[p,q]
        

print(new_train)












d_ly_13_f = ly_13_f.describe()
print(d_ly_13_f)

i=30



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_13_f.iloc[p,q]
        

print(new_train)










d_ly_14_f = ly_14_f.describe()
print(d_ly_14_f)

i=31



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_14_f.iloc[p,q]
        

print(new_train)












d_ly_15_f = ly_15_f.describe()
print(d_ly_15_f)

i=32



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_ly_15_f.iloc[p,q]
        

print(new_train)





























d_sit_4_f = sit_4_f.describe()
print(d_sit_4_f)

i=33



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_4_f.iloc[p,q]
        

print(new_train)












d_sit_5_f = sit_5_f.describe()
print(d_sit_5_f)

i=34



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_5_f.iloc[p,q]
        

print(new_train)


















d_sit_6_f = sit_6_f.describe()
print(d_sit_6_f)

i=35



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_6_f.iloc[p,q]
        

print(new_train)



















d_sit_7_f = sit_7_f.describe()
print(d_sit_7_f)

i=36



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_7_f.iloc[p,q]
        

print(new_train)
















d_sit_8_f = sit_8_f.describe()
print(d_sit_8_f)

i=37



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_8_f.iloc[p,q]
        

print(new_train)










d_sit_9_f = sit_9_f.describe()
print(d_sit_9_f)

i=38



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_9_f.iloc[p,q]
        

print(new_train)











d_sit_10_f = sit_10_f.describe()
print(d_sit_10_f)

i=39



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_10_f.iloc[p,q]
        

print(new_train)











d_sit_11_f = sit_11_f.describe()
print(d_sit_11_f)

i=40



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_11_f.iloc[p,q]
        

print(new_train)












d_sit_12_f = sit_12_f.describe()
print(d_sit_12_f)

i=41



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_12_f.iloc[p,q]
        

print(new_train)












d_sit_13_f = sit_13_f.describe()
print(d_sit_13_f)

i=42



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_13_f.iloc[p,q]
        

print(new_train)










d_sit_14_f = sit_14_f.describe()
print(d_sit_14_f)

i=43



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_14_f.iloc[p,q]
        

print(new_train)












d_sit_15_f = sit_15_f.describe()
print(d_sit_15_f)

i=44



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_sit_15_f.iloc[p,q]
        

print(new_train)































d_stand_4_f = stand_4_f.describe()
print(d_stand_4_f)

i=45



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_4_f.iloc[p,q]
        

print(new_train)












d_stand_5_f = stand_5_f.describe()
print(d_stand_5_f)

i=46



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_5_f.iloc[p,q]
        

print(new_train)


















d_stand_6_f = stand_6_f.describe()
print(d_stand_6_f)

i=47



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_6_f.iloc[p,q]
        

print(new_train)



















d_stand_7_f = stand_7_f.describe()
print(d_stand_7_f)

i=48



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_7_f.iloc[p,q]
        

print(new_train)
















d_stand_8_f = stand_8_f.describe()
print(d_stand_8_f)

i=49



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_8_f.iloc[p,q]
        

print(new_train)










d_stand_9_f = stand_9_f.describe()
print(d_stand_9_f)

i=50



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_9_f.iloc[p,q]
        

print(new_train)











d_stand_10_f = stand_10_f.describe()
print(d_stand_10_f)

i=51



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_10_f.iloc[p,q]
        

print(new_train)











d_stand_11_f = stand_11_f.describe()
print(d_stand_11_f)

i=52



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_11_f.iloc[p,q]
        

print(new_train)












d_stand_12_f = stand_12_f.describe()
print(d_stand_12_f)

i=53



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_12_f.iloc[p,q]
        

print(new_train)












d_stand_13_f = stand_13_f.describe()
print(d_stand_13_f)

i=54



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_13_f.iloc[p,q]
        

print(new_train)










d_stand_14_f = stand_14_f.describe()
print(d_stand_14_f)

i=55



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_14_f.iloc[p,q]
        

print(new_train)












d_stand_15_f = stand_15_f.describe()
print(d_stand_15_f)

i=56



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_stand_15_f.iloc[p,q]
        

print(new_train)



































d_wa_4_f = wa_4_f.describe()
print(d_wa_4_f)

i=57



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_4_f.iloc[p,q]
        

print(new_train)












d_wa_5_f = wa_5_f.describe()
print(d_wa_5_f)

i=58



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_5_f.iloc[p,q]
        

print(new_train)


















d_wa_6_f = wa_6_f.describe()
print(d_wa_6_f)

i=59



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_6_f.iloc[p,q]
        

print(new_train)



















d_wa_7_f = wa_7_f.describe()
print(d_wa_7_f)

i=60



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_7_f.iloc[p,q]
        

print(new_train)
















d_wa_8_f = wa_8_f.describe()
print(d_wa_8_f)

i=61



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_8_f.iloc[p,q]
        

print(new_train)










d_wa_9_f = wa_9_f.describe()
print(d_wa_9_f)

i=62



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_9_f.iloc[p,q]
        

print(new_train)











d_wa_10_f = wa_10_f.describe()
print(d_wa_10_f)

i=63



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_10_f.iloc[p,q]
        

print(new_train)











d_wa_11_f = wa_11_f.describe()
print(d_wa_11_f)

i=64



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_11_f.iloc[p,q]
        

print(new_train)












d_wa_12_f = wa_12_f.describe()
print(d_wa_12_f)

i=65



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_12_f.iloc[p,q]
        

print(new_train)












d_wa_13_f = wa_13_f.describe()
print(d_wa_13_f)

i=66



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_13_f.iloc[p,q]
        

print(new_train)










d_wa_14_f = wa_14_f.describe()
print(d_wa_14_f)

i=67



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_14_f.iloc[p,q]
        

print(new_train)












d_wa_15_f = wa_15_f.describe()
print(d_wa_15_f)

i=68



j=0
q=0
p=0
for j in col:
    if j == 0 or j == 1 or j == 2:
        q=0
    elif j == 3 or j == 4 or j == 5:
        q=1
    elif j == 6 or j == 7 or j == 8:
        q=5
    elif j == 9 or j == 10 or j == 11:
        q=6
    elif j == 12 or j == 13 or j == 14:
        q=7
    elif j == 15 or j == 16 or j == 17:
        q=11
    
    if j == 0 or j == 3 or j == 6 or j == 9 or j == 12 or j == 15:
        p=1
    elif j == 1 or j == 4 or j == 7 or j == 10 or j == 13 or j == 16:
        p=2
    else:
        p=7
    
    new_train.iloc[i,j] = d_wa_15_f.iloc[p,q]
        

print(new_train)
















new_train.to_csv('New_Train_Set.csv')


"""
Exporting the file to csv for scatterplots

"""












