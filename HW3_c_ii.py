# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:15:34 2020

@author: DHRUV
"""


"""
HW3 (c) (ii)

"""

"""
We have 88 instances/datasets. Each instance has 6 features. For each instance, we'll summarize the data
for each feature of an instance. So for instance 1, say, we have 6 features from feature_1, feature_2,....
......, to feature_6. feature_1 has it's own min, max, mean, median, standard deviation, first quartile and third 
quartile. Each feature, thus, in each instance, has 7 feature summary. 7*6 = 42 columns thus exist in our
data summary. The total rows are the total instances, that is, 88. 

So the data summary has dimension 88 x 42 size.

Also as we have to summarize for each instance, we assume that no training, test splitting is needed here, as,
in the question the first few instances for each action were characterized as test and the remaining as train.
Here as all instances are to be summarized, this is the summary of the entire data, including test and train 
instances, in general, for every single action.

All the datasets have been, for python and pandas use, appropriately modified and named in Excel itself

"""

import pandas as pd
import numpy as np

b1_1 = pd.read_csv('bending1\\test\\dataset1.csv')
print(b1_1)
b1_2 = pd.read_csv('bending1\\test\\dataset2.csv')
print(b1_2)
b1_3 = pd.read_csv('bending1\\training\\dataset3.csv')
print(b1_3)
b1_4 = pd.read_csv('bending1\\training\\dataset4.csv')
print(b1_4)
b1_5 = pd.read_csv('bending1\\training\\dataset5.csv')
print(b1_5)
b1_6 = pd.read_csv('bending1\\training\\dataset6.csv')
print(b1_6)
b1_7 = pd.read_csv('bending1\\training\\dataset7.csv')
print(b1_7)



b2_1 = pd.read_csv('bending2\\test\\dataset1.csv')
print(b2_1)
b2_2 = pd.read_csv('bending2\\test\\dataset2.csv')
print(b2_2)
b2_3 = pd.read_csv('bending2\\training\\dataset3.csv')
print(b2_3)
b2_4 = pd.read_csv('bending2\\training\\dataset4.csv')
print(b2_4)
b2_5 = pd.read_csv('bending2\\training\\dataset5.csv')
print(b2_5)
b2_6 = pd.read_csv('bending2\\training\\dataset6.csv')
print(b2_6)


cy_1 = pd.read_csv('cycling\\test\\dataset1.csv')
print(cy_1)
cy_2 = pd.read_csv('cycling\\test\\dataset2.csv')
print(cy_2)
cy_3 = pd.read_csv('cycling\\test\\dataset3.csv')
print(cy_3)
cy_4 = pd.read_csv('cycling\\training\\dataset4.csv')
print(cy_4)
cy_5 = pd.read_csv('cycling\\training\\dataset5.csv')
print(cy_5)
cy_6 = pd.read_csv('cycling\\training\\dataset6.csv')
print(cy_6)
cy_7 = pd.read_csv('cycling\\training\\dataset7.csv')
print(cy_7)
cy_8 = pd.read_csv('cycling\\training\\dataset8.csv')
print(cy_8)
cy_9 = pd.read_csv('cycling\\training\\dataset9.csv')
print(cy_9)
cy_10 = pd.read_csv('cycling\\training\\dataset10.csv')
print(cy_10)
cy_11 = pd.read_csv('cycling\\training\\dataset11.csv')
print(cy_11)
cy_12 = pd.read_csv('cycling\\training\\dataset12.csv')
print(cy_12)
cy_13 = pd.read_csv('cycling\\training\\dataset13.csv')
print(cy_13)
cy_14 = pd.read_csv('cycling\\training\\dataset14.csv')
print(cy_14)
cy_15 = pd.read_csv('cycling\\training\\dataset15.csv')
print(cy_15)




ly_1 = pd.read_csv('lying\\test\\dataset1.csv')
print(ly_1)
ly_2 = pd.read_csv('lying\\test\\dataset2.csv')
print(ly_2)
ly_3 = pd.read_csv('lying\\test\\dataset3.csv')
print(ly_3)
ly_4 = pd.read_csv('lying\\training\\dataset4.csv')
print(ly_4)
ly_5 = pd.read_csv('lying\\training\\dataset5.csv')
print(ly_5)
ly_6 = pd.read_csv('lying\\training\\dataset6.csv')
print(ly_6)
ly_7 = pd.read_csv('lying\\training\\dataset7.csv')
print(ly_7)
ly_8 = pd.read_csv('lying\\training\\dataset8.csv')
print(ly_8)
ly_9 = pd.read_csv('lying\\training\\dataset9.csv')
print(ly_9)
ly_10 = pd.read_csv('lying\\training\\dataset10.csv')
print(ly_10)
ly_11 = pd.read_csv('lying\\training\\dataset11.csv')
print(ly_11)
ly_12 = pd.read_csv('lying\\training\\dataset12.csv')
print(ly_12)
ly_13 = pd.read_csv('lying\\training\\dataset13.csv')
print(ly_13)
ly_14 = pd.read_csv('lying\\training\\dataset14.csv')
print(ly_14)
ly_15 = pd.read_csv('lying\\training\\dataset15.csv')
print(ly_15)






sit_1 = pd.read_csv('sitting\\test\\dataset1.csv')
print(sit_1)
sit_2 = pd.read_csv('sitting\\test\\dataset2.csv')
print(sit_2)
sit_3 = pd.read_csv('sitting\\test\\dataset3.csv')
print(sit_3)
sit_4 = pd.read_csv('sitting\\training\\dataset4.csv')
print(sit_4)
sit_5 = pd.read_csv('sitting\\training\\dataset5.csv')
print(sit_5)
sit_6 = pd.read_csv('sitting\\training\\dataset6.csv')
print(sit_6)
sit_7 = pd.read_csv('sitting\\training\\dataset7.csv')
print(sit_7)
sit_8 = pd.read_csv('sitting\\training\\dataset8.csv')
print(sit_8)
sit_9 = pd.read_csv('sitting\\training\\dataset9.csv')
print(sit_9)
sit_10 = pd.read_csv('sitting\\training\\dataset10.csv')
print(sit_10)
sit_11 = pd.read_csv('sitting\\training\\dataset11.csv')
print(sit_11)
sit_12 = pd.read_csv('sitting\\training\\dataset12.csv')
print(sit_12)
sit_13 = pd.read_csv('sitting\\training\\dataset13.csv')
print(sit_13)
sit_14 = pd.read_csv('sitting\\training\\dataset14.csv')
print(sit_14)
sit_15 = pd.read_csv('sitting\\training\\dataset15.csv')
print(sit_15)




stand_1 = pd.read_csv('standing\\test\\dataset1.csv')
print(stand_1)
stand_2 = pd.read_csv('standing\\test\\dataset2.csv')
print(stand_2)
stand_3 = pd.read_csv('standing\\test\\dataset3.csv')
print(stand_3)
stand_4 = pd.read_csv('standing\\training\\dataset4.csv')
print(stand_4)
stand_5 = pd.read_csv('standing\\training\\dataset5.csv')
print(stand_5)
stand_6 = pd.read_csv('standing\\training\\dataset6.csv')
print(stand_6)
stand_7 = pd.read_csv('standing\\training\\dataset7.csv')
print(stand_7)
stand_8 = pd.read_csv('standing\\training\\dataset8.csv')
print(stand_8)
stand_9 = pd.read_csv('standing\\training\\dataset9.csv')
print(stand_9)
stand_10 = pd.read_csv('standing\\training\\dataset10.csv')
print(stand_10)
stand_11 = pd.read_csv('standing\\training\\dataset11.csv')
print(stand_11)
stand_12 = pd.read_csv('standing\\training\\dataset12.csv')
print(stand_12)
stand_13 = pd.read_csv('standing\\training\\dataset13.csv')
print(stand_13)
stand_14 = pd.read_csv('standing\\training\\dataset14.csv')
print(stand_14)
stand_15 = pd.read_csv('standing\\training\\dataset15.csv')
print(stand_15)






wa_1 = pd.read_csv('walking\\test\\dataset1.csv')
print(wa_1)
wa_2 = pd.read_csv('walking\\test\\dataset2.csv')
print(wa_2)
wa_3 = pd.read_csv('walking\\test\\dataset3.csv')
print(wa_3)
wa_4 = pd.read_csv('walking\\training\\dataset4.csv')
print(wa_4)
wa_5 = pd.read_csv('walking\\training\\dataset5.csv')
print(wa_5)
wa_6 = pd.read_csv('walking\\training\\dataset6.csv')
print(wa_6)
wa_7 = pd.read_csv('walking\\training\\dataset7.csv')
print(wa_7)
wa_8 = pd.read_csv('walking\\training\\dataset8.csv')
print(wa_8)
wa_9 = pd.read_csv('walking\\training\\dataset9.csv')
print(wa_9)
wa_10 = pd.read_csv('walking\\training\\dataset10.csv')
print(wa_10)
wa_11 = pd.read_csv('walking\\training\\dataset11.csv')
print(wa_11)
wa_12 = pd.read_csv('walking\\training\\dataset12.csv')
print(wa_12)
wa_13 = pd.read_csv('walking\\training\\dataset13.csv')
print(wa_13)
wa_14 = pd.read_csv('walking\\training\\dataset14.csv')
print(wa_14)
wa_15 = pd.read_csv('walking\\training\\dataset15.csv')
print(wa_15)



headers = ['avg_rss12_mean', 'avg_rss12_std', 'avg_rss12_min', 'avg_rss12_q1','avg_rss12_median', 'avg_rss12_q3','avg_rss12_max','var_rss12_mean', 'var_rss12_std', 'var_rss12_min', 'var_rss12_q1','var_rss12_median', 'var_rss12_q3','var_rss12_max','avg_rss13_mean', 'avg_rss13_std', 'avg_rss13_min', 'avg_rss13_q1','avg_rss13_median', 'avg_rss13_q3','avg_rss13_max','var_rss13_mean', 'var_rss13_std', 'var_rss13_min', 'var_rss13_q1','var_rss13_median', 'var_rss13_q3','var_rss13_max','avg_rss23_mean', 'avg_rss23_std', 'avg_rss23_min', 'avg_rss23_q1','avg_rss23_median', 'avg_rss23_q3','avg_rss23_max','var_rss23_mean', 'var_rss23_std', 'var_rss23_min', 'var_rss23_q1','var_rss23_median', 'var_rss23_q3','var_rss23_max']
names_of_instances = ['b1_1','b1_2','b1_3','b1_4','b1_5','b1_6','b1_7','b2_1','b2_2','b2_3','b2_4','b2_5','b2_6','cy_1','cy_2','cy_3','cy_4','cy_5','cy_6','cy_7','cy_8','cy_9','cy_10','cy_11','cy_12','cy_13','cy_14','cy_15','ly_1','ly_2','ly_3','ly_4','ly_5','ly_6','ly_7','ly_8','ly_9','ly_10','ly_11','ly_12','ly_13','ly_14','ly_15','sit_1','sit_2','sit_3','sit_4','sit_5','sit_6','sit_7','sit_8','sit_9','sit_10','sit_11','sit_12','sit_13','sit_14','sit_15','stand_1','stand_2','stand_3','stand_4','stand_5','stand_6','stand_7','stand_8','stand_9','stand_10','stand_11','stand_12','stand_13','stand_14','stand_15','wa_1','wa_2','wa_3','wa_4','wa_5','wa_6','wa_7','wa_8','wa_9','wa_10','wa_11','wa_12','wa_13','wa_14','wa_15']
final_df = pd.DataFrame(columns = headers, index = names_of_instances)
print(final_df)


d_b1_1 = b1_1.drop(columns = ['time_b1_1']).describe()
d_b1_1 = d_b1_1.iloc[1:8,:]
d_b1_1_flat = d_b1_1.to_numpy().flatten('F')
final_df.iloc[0,:] = d_b1_1_flat



d_b1_2 = b1_2.drop(columns = ['time_b1_2']).describe()
d_b1_2 = d_b1_2.iloc[1:8,:]
d_b1_2_flat = d_b1_2.to_numpy().flatten('F')
final_df.iloc[1,:] = d_b1_2_flat



d_b1_3 = b1_3.drop(columns = ['time_b1_3']).describe()
d_b1_3 = d_b1_3.iloc[1:8,:]
d_b1_3_flat = d_b1_3.to_numpy().flatten('F')
final_df.iloc[2,:] = d_b1_3_flat



d_b1_4 = b1_4.drop(columns = ['time_b1_4']).describe()
d_b1_4 = d_b1_4.iloc[1:8,:]
d_b1_4_flat = d_b1_4.to_numpy().flatten('F')
final_df.iloc[3,:] = d_b1_4_flat


d_b1_5 = b1_5.drop(columns = ['time_b1_5']).describe()
d_b1_5 = d_b1_5.iloc[1:8,:]
d_b1_5_flat = d_b1_5.to_numpy().flatten('F')
final_df.iloc[4,:] = d_b1_5_flat


d_b1_6 = b1_6.drop(columns = ['time_b1_6']).describe()
d_b1_6 = d_b1_6.iloc[1:8,:]
d_b1_6_flat = d_b1_6.to_numpy().flatten('F')
final_df.iloc[5,:] = d_b1_6_flat


d_b1_7 = b1_7.drop(columns = ['time_b1_7']).describe()
d_b1_7 = d_b1_7.iloc[1:8,:]
d_b1_7_flat = d_b1_7.to_numpy().flatten('F')
final_df.iloc[6,:] = d_b1_7_flat









d_b2_1 = b2_1.drop(columns = ['time_b2_1']).describe()
d_b2_1 = d_b2_1.iloc[1:8,:]
d_b2_1_flat = d_b2_1.to_numpy().flatten('F')
final_df.iloc[7,:] = d_b2_1_flat


d_b2_2 = b2_2.drop(columns = ['time_b2_2']).describe()
d_b2_2 = d_b2_2.iloc[1:8,:]
d_b2_2_flat = d_b2_2.to_numpy().flatten('F')
final_df.iloc[8,:] = d_b2_2_flat


d_b2_3 = b2_3.drop(columns = ['time_b2_3']).describe()
d_b2_3 = d_b2_3.iloc[1:8,:]
d_b2_3_flat = d_b2_3.to_numpy().flatten('F')
final_df.iloc[9,:] = d_b2_3_flat


d_b2_4 = b2_4.drop(columns = ['time_b2_4']).describe()
d_b2_4 = d_b2_4.iloc[1:8,:]
d_b2_4_flat = d_b2_4.to_numpy().flatten('F')
final_df.iloc[10,:] = d_b2_4_flat

d_b2_5 = b2_5.drop(columns = ['time_b2_5']).describe()
d_b2_5 = d_b2_5.iloc[1:8,:]
d_b2_5_flat = d_b2_5.to_numpy().flatten('F')
final_df.iloc[11,:] = d_b2_5_flat


d_b2_6 = b2_6.drop(columns = ['time_b2_6']).describe()
d_b2_6 = d_b2_6.iloc[1:8,:]
d_b2_6_flat = d_b2_6.to_numpy().flatten('F')
final_df.iloc[12,:] = d_b2_6_flat












d_cy_1 = cy_1.drop(columns = ['time_cy_1']).describe()
d_cy_1 = d_cy_1.iloc[1:8,:]
d_cy_1_flat = d_cy_1.to_numpy().flatten('F')
final_df.iloc[13,:] = d_cy_1_flat


d_cy_2 = cy_2.drop(columns = ['time_cy_2']).describe()
d_cy_2 = d_cy_2.iloc[1:8,:]
d_cy_2_flat = d_cy_2.to_numpy().flatten('F')
final_df.iloc[14,:] = d_cy_2_flat


d_cy_3 = cy_3.drop(columns = ['time_cy_3']).describe()
d_cy_3 = d_cy_3.iloc[1:8,:]
d_cy_3_flat = d_cy_3.to_numpy().flatten('F')
final_df.iloc[15,:] = d_cy_3_flat


d_cy_4 = cy_4.drop(columns = ['time_cy_4']).describe()
d_cy_4 = d_cy_4.iloc[1:8,:]
d_cy_4_flat = d_cy_4.to_numpy().flatten('F')
final_df.iloc[16,:] = d_cy_4_flat


d_cy_5 = cy_5.drop(columns = ['time_cy_5']).describe()
d_cy_5 = d_cy_5.iloc[1:8,:]
d_cy_5_flat = d_cy_5.to_numpy().flatten('F')
final_df.iloc[17,:] = d_cy_5_flat


d_cy_6 = cy_6.drop(columns = ['time_cy_6']).describe()
d_cy_6 = d_cy_6.iloc[1:8,:]
d_cy_6_flat = d_cy_6.to_numpy().flatten('F')
final_df.iloc[18,:] = d_cy_6_flat


d_cy_7 = cy_7.drop(columns = ['time_cy_7']).describe()
d_cy_7 = d_cy_7.iloc[1:8,:]
d_cy_7_flat = d_cy_7.to_numpy().flatten('F')
final_df.iloc[19,:] = d_cy_7_flat


d_cy_8 = cy_8.drop(columns = ['time_cy_8']).describe()
d_cy_8 = d_cy_8.iloc[1:8,:]
d_cy_8_flat = d_cy_8.to_numpy().flatten('F')
final_df.iloc[20,:] = d_cy_8_flat


d_cy_9 = cy_9.drop(columns = ['time_cy_9']).describe()
d_cy_9 = d_cy_9.iloc[1:8,:]
d_cy_9_flat = d_cy_9.to_numpy().flatten('F')
final_df.iloc[21,:] = d_cy_9_flat


d_cy_10 = cy_10.drop(columns = ['time_cy_10']).describe()
d_cy_10 = d_cy_10.iloc[1:8,:]
d_cy_10_flat = d_cy_10.to_numpy().flatten('F')
final_df.iloc[22,:] = d_cy_10_flat


d_cy_11 = cy_11.drop(columns = ['time_cy_11']).describe()
d_cy_11 = d_cy_11.iloc[1:8,:]
d_cy_11_flat = d_cy_11.to_numpy().flatten('F')
final_df.iloc[23,:] = d_cy_11_flat


d_cy_12 = cy_12.drop(columns = ['time_cy_12']).describe()
d_cy_12 = d_cy_12.iloc[1:8,:]
d_cy_12_flat = d_cy_12.to_numpy().flatten('F')
final_df.iloc[24,:] = d_cy_12_flat


d_cy_13 = cy_13.drop(columns = ['time_cy_13']).describe()
d_cy_13 = d_cy_13.iloc[1:8,:]
d_cy_13_flat = d_cy_13.to_numpy().flatten('F')
final_df.iloc[25,:] = d_cy_13_flat


d_cy_14 = cy_14.drop(columns = ['time_cy_14']).describe()
d_cy_14 = d_cy_14.iloc[1:8,:]
d_cy_14_flat = d_cy_14.to_numpy().flatten('F')
final_df.iloc[26,:] = d_cy_14_flat



d_cy_15 = cy_15.drop(columns = ['time_cy_15']).describe()
d_cy_15 = d_cy_15.iloc[1:8,:]
d_cy_15_flat = d_cy_15.to_numpy().flatten('F')
final_df.iloc[27,:] = d_cy_15_flat


















d_ly_1 = ly_1.drop(columns = ['time_ly_1']).describe()
d_ly_1 = d_ly_1.iloc[1:8,:]
d_ly_1_flat = d_ly_1.to_numpy().flatten('F')
final_df.iloc[28,:] = d_ly_1_flat


d_ly_2 = ly_2.drop(columns = ['time_ly_2']).describe()
d_ly_2 = d_ly_2.iloc[1:8,:]
d_ly_2_flat = d_ly_2.to_numpy().flatten('F')
final_df.iloc[29,:] = d_ly_2_flat


d_ly_3 = ly_3.drop(columns = ['time_ly_3']).describe()
d_ly_3 = d_ly_3.iloc[1:8,:]
d_ly_3_flat = d_ly_3.to_numpy().flatten('F')
final_df.iloc[30,:] = d_ly_3_flat


d_ly_4 = ly_4.drop(columns = ['time_ly_4']).describe()
d_ly_4 = d_ly_4.iloc[1:8,:]
d_ly_4_flat = d_ly_4.to_numpy().flatten('F')
final_df.iloc[31,:] = d_ly_4_flat


d_ly_5 = ly_5.drop(columns = ['time_ly_5']).describe()
d_ly_5 = d_ly_5.iloc[1:8,:]
d_ly_5_flat = d_ly_5.to_numpy().flatten('F')
final_df.iloc[32,:] = d_ly_5_flat


d_ly_6 = ly_6.drop(columns = ['time_ly_6']).describe()
d_ly_6 = d_ly_6.iloc[1:8,:]
d_ly_6_flat = d_ly_6.to_numpy().flatten('F')
final_df.iloc[33,:] = d_ly_6_flat


d_ly_7 = ly_7.drop(columns = ['time_ly_7']).describe()
d_ly_7 = d_ly_7.iloc[1:8,:]
d_ly_7_flat = d_ly_7.to_numpy().flatten('F')
final_df.iloc[34,:] = d_ly_7_flat


d_ly_8 = ly_8.drop(columns = ['time_ly_8']).describe()
d_ly_8 = d_ly_8.iloc[1:8,:]
d_ly_8_flat = d_ly_8.to_numpy().flatten('F')
final_df.iloc[35,:] = d_ly_8_flat


d_ly_9 = ly_9.drop(columns = ['time_ly_9']).describe()
d_ly_9 = d_ly_9.iloc[1:8,:]
d_ly_9_flat = d_ly_9.to_numpy().flatten('F')
final_df.iloc[36,:] = d_ly_9_flat


d_ly_10 = ly_10.drop(columns = ['time_ly_10']).describe()
d_ly_10 = d_ly_10.iloc[1:8,:]
d_ly_10_flat = d_ly_10.to_numpy().flatten('F')
final_df.iloc[37,:] = d_ly_10_flat


d_ly_11 = ly_11.drop(columns = ['time_ly_11']).describe()
d_ly_11 = d_ly_11.iloc[1:8,:]
d_ly_11_flat = d_ly_11.to_numpy().flatten('F')
final_df.iloc[38,:] = d_ly_11_flat


d_ly_12 = ly_12.drop(columns = ['time_ly_12']).describe()
d_ly_12 = d_ly_12.iloc[1:8,:]
d_ly_12_flat = d_ly_12.to_numpy().flatten('F')
final_df.iloc[39,:] = d_ly_12_flat


d_ly_13 = ly_13.drop(columns = ['time_ly_13']).describe()
d_ly_13 = d_ly_13.iloc[1:8,:]
d_ly_13_flat = d_ly_13.to_numpy().flatten('F')
final_df.iloc[40,:] = d_ly_13_flat


d_ly_14 = ly_14.drop(columns = ['time_ly_14']).describe()
d_ly_14 = d_ly_14.iloc[1:8,:]
d_ly_14_flat = d_ly_14.to_numpy().flatten('F')
final_df.iloc[41,:] = d_ly_14_flat



d_ly_15 = ly_15.drop(columns = ['time_ly_15']).describe()
d_ly_15 = d_ly_15.iloc[1:8,:]
d_ly_15_flat = d_ly_15.to_numpy().flatten('F')
final_df.iloc[42,:] = d_ly_15_flat




















d_sit_1 = sit_1.drop(columns = ['time_sit_1']).describe()
d_sit_1 = d_sit_1.iloc[1:8,:]
d_sit_1_flat = d_sit_1.to_numpy().flatten('F')
final_df.iloc[43,:] = d_sit_1_flat


d_sit_2 = sit_2.drop(columns = ['time_sit_2']).describe()
d_sit_2 = d_sit_2.iloc[1:8,:]
d_sit_2_flat = d_sit_2.to_numpy().flatten('F')
final_df.iloc[44,:] = d_sit_2_flat


d_sit_3 = sit_3.drop(columns = ['time_sit_3']).describe()
d_sit_3 = d_sit_3.iloc[1:8,:]
d_sit_3_flat = d_sit_3.to_numpy().flatten('F')
final_df.iloc[45,:] = d_sit_3_flat


d_sit_4 = sit_4.drop(columns = ['time_sit_4']).describe()
d_sit_4 = d_sit_4.iloc[1:8,:]
d_sit_4_flat = d_sit_4.to_numpy().flatten('F')
final_df.iloc[46,:] = d_sit_4_flat


d_sit_5 = sit_5.drop(columns = ['time_sit_5']).describe()
d_sit_5 = d_sit_5.iloc[1:8,:]
d_sit_5_flat = d_sit_5.to_numpy().flatten('F')
final_df.iloc[47,:] = d_sit_5_flat


d_sit_6 = sit_6.drop(columns = ['time_sit_6']).describe()
d_sit_6 = d_sit_6.iloc[1:8,:]
d_sit_6_flat = d_sit_6.to_numpy().flatten('F')
final_df.iloc[48,:] = d_sit_6_flat


d_sit_7 = sit_7.drop(columns = ['time_sit_7']).describe()
d_sit_7 = d_sit_7.iloc[1:8,:]
d_sit_7_flat = d_sit_7.to_numpy().flatten('F')
final_df.iloc[49,:] = d_sit_7_flat


d_sit_8 = sit_8.drop(columns = ['time_sit_8']).describe()
d_sit_8 = d_sit_8.iloc[1:8,:]
d_sit_8_flat = d_sit_8.to_numpy().flatten('F')
final_df.iloc[50,:] = d_sit_8_flat


d_sit_9 = sit_9.drop(columns = ['time_sit_9']).describe()
d_sit_9 = d_sit_9.iloc[1:8,:]
d_sit_9_flat = d_sit_9.to_numpy().flatten('F')
final_df.iloc[51,:] = d_sit_9_flat


d_sit_10 = sit_10.drop(columns = ['time_sit_10']).describe()
d_sit_10 = d_sit_10.iloc[1:8,:]
d_sit_10_flat = d_sit_10.to_numpy().flatten('F')
final_df.iloc[52,:] = d_sit_10_flat


d_sit_11 = sit_11.drop(columns = ['time_sit_11']).describe()
d_sit_11 = d_sit_11.iloc[1:8,:]
d_sit_11_flat = d_sit_11.to_numpy().flatten('F')
final_df.iloc[53,:] = d_sit_11_flat


d_sit_12 = sit_12.drop(columns = ['time_sit_12']).describe()
d_sit_12 = d_sit_12.iloc[1:8,:]
d_sit_12_flat = d_sit_12.to_numpy().flatten('F')
final_df.iloc[54,:] = d_sit_12_flat


d_sit_13 = sit_13.drop(columns = ['time_sit_13']).describe()
d_sit_13 = d_sit_13.iloc[1:8,:]
d_sit_13_flat = d_sit_13.to_numpy().flatten('F')
final_df.iloc[55,:] = d_sit_13_flat


d_sit_14 = sit_14.drop(columns = ['time_sit_14']).describe()
d_sit_14 = d_sit_14.iloc[1:8,:]
d_sit_14_flat = d_sit_14.to_numpy().flatten('F')
final_df.iloc[56,:] = d_sit_14_flat



d_sit_15 = sit_15.drop(columns = ['time_sit_15']).describe()
d_sit_15 = d_sit_15.iloc[1:8,:]
d_sit_15_flat = d_sit_15.to_numpy().flatten('F')
final_df.iloc[57,:] = d_sit_15_flat












d_stand_1 = stand_1.drop(columns = ['time_stand_1']).describe()
d_stand_1 = d_stand_1.iloc[1:8,:]
d_stand_1_flat = d_stand_1.to_numpy().flatten('F')
final_df.iloc[58,:] = d_stand_1_flat


d_stand_2 = stand_2.drop(columns = ['time_stand_2']).describe()
d_stand_2 = d_stand_2.iloc[1:8,:]
d_stand_2_flat = d_stand_2.to_numpy().flatten('F')
final_df.iloc[59,:] = d_stand_2_flat


d_stand_3 = stand_3.drop(columns = ['time_stand_3']).describe()
d_stand_3 = d_stand_3.iloc[1:8,:]
d_stand_3_flat = d_stand_3.to_numpy().flatten('F')
final_df.iloc[60,:] = d_stand_3_flat


d_stand_4 = stand_4.drop(columns = ['time_stand_4']).describe()
d_stand_4 = d_stand_4.iloc[1:8,:]
d_stand_4_flat = d_stand_4.to_numpy().flatten('F')
final_df.iloc[61,:] = d_stand_4_flat


d_stand_5 = stand_5.drop(columns = ['time_stand_5']).describe()
d_stand_5 = d_stand_5.iloc[1:8,:]
d_stand_5_flat = d_stand_5.to_numpy().flatten('F')
final_df.iloc[62,:] = d_stand_5_flat


d_stand_6 = stand_6.drop(columns = ['time_stand_6']).describe()
d_stand_6 = d_stand_6.iloc[1:8,:]
d_stand_6_flat = d_stand_6.to_numpy().flatten('F')
final_df.iloc[63,:] = d_stand_6_flat


d_stand_7 = stand_7.drop(columns = ['time_stand_7']).describe()
d_stand_7 = d_stand_7.iloc[1:8,:]
d_stand_7_flat = d_stand_7.to_numpy().flatten('F')
final_df.iloc[64,:] = d_stand_7_flat


d_stand_8 = stand_8.drop(columns = ['time_stand_8']).describe()
d_stand_8 = d_stand_8.iloc[1:8,:]
d_stand_8_flat = d_stand_8.to_numpy().flatten('F')
final_df.iloc[65,:] = d_stand_8_flat


d_stand_9 = stand_9.drop(columns = ['time_stand_9']).describe()
d_stand_9 = d_stand_9.iloc[1:8,:]
d_stand_9_flat = d_stand_9.to_numpy().flatten('F')
final_df.iloc[66,:] = d_stand_9_flat


d_stand_10 = stand_10.drop(columns = ['time_stand_10']).describe()
d_stand_10 = d_stand_10.iloc[1:8,:]
d_stand_10_flat = d_stand_10.to_numpy().flatten('F')
final_df.iloc[67,:] = d_stand_10_flat


d_stand_11 = stand_11.drop(columns = ['time_stand_11']).describe()
d_stand_11 = d_stand_11.iloc[1:8,:]
d_stand_11_flat = d_stand_11.to_numpy().flatten('F')
final_df.iloc[68,:] = d_stand_11_flat


d_stand_12 = stand_12.drop(columns = ['time_stand_12']).describe()
d_stand_12 = d_stand_12.iloc[1:8,:]
d_stand_12_flat = d_stand_12.to_numpy().flatten('F')
final_df.iloc[69,:] = d_stand_12_flat


d_stand_13 = stand_13.drop(columns = ['time_stand_13']).describe()
d_stand_13 = d_stand_13.iloc[1:8,:]
d_stand_13_flat = d_stand_13.to_numpy().flatten('F')
final_df.iloc[70,:] = d_stand_13_flat


d_stand_14 = stand_14.drop(columns = ['time_stand_14']).describe()
d_stand_14 = d_stand_14.iloc[1:8,:]
d_stand_14_flat = d_stand_14.to_numpy().flatten('F')
final_df.iloc[71,:] = d_stand_14_flat



d_stand_15 = stand_15.drop(columns = ['time_stand_15']).describe()
d_stand_15 = d_stand_15.iloc[1:8,:]
d_stand_15_flat = d_stand_15.to_numpy().flatten('F')
final_df.iloc[72,:] = d_stand_15_flat

















d_wa_1 = wa_1.drop(columns = ['time_wa_1']).describe()
d_wa_1 = d_wa_1.iloc[1:8,:]
d_wa_1_flat = d_wa_1.to_numpy().flatten('F')
final_df.iloc[73,:] = d_wa_1_flat


d_wa_2 = wa_2.drop(columns = ['time_wa_2']).describe()
d_wa_2 = d_wa_2.iloc[1:8,:]
d_wa_2_flat = d_wa_2.to_numpy().flatten('F')
final_df.iloc[74,:] = d_wa_2_flat


d_wa_3 = wa_3.drop(columns = ['time_wa_3']).describe()
d_wa_3 = d_wa_3.iloc[1:8,:]
d_wa_3_flat = d_wa_3.to_numpy().flatten('F')
final_df.iloc[75,:] = d_wa_3_flat


d_wa_4 = wa_4.drop(columns = ['time_wa_4']).describe()
d_wa_4 = d_wa_4.iloc[1:8,:]
d_wa_4_flat = d_wa_4.to_numpy().flatten('F')
final_df.iloc[76,:] = d_wa_4_flat


d_wa_5 = wa_5.drop(columns = ['time_wa_5']).describe()
d_wa_5 = d_wa_5.iloc[1:8,:]
d_wa_5_flat = d_wa_5.to_numpy().flatten('F')
final_df.iloc[77,:] = d_wa_5_flat


d_wa_6 = wa_6.drop(columns = ['time_wa_6']).describe()
d_wa_6 = d_wa_6.iloc[1:8,:]
d_wa_6_flat = d_wa_6.to_numpy().flatten('F')
final_df.iloc[78,:] = d_wa_6_flat


d_wa_7 = wa_7.drop(columns = ['time_wa_7']).describe()
d_wa_7 = d_wa_7.iloc[1:8,:]
d_wa_7_flat = d_wa_7.to_numpy().flatten('F')
final_df.iloc[79,:] = d_wa_7_flat


d_wa_8 = wa_8.drop(columns = ['time_wa_8']).describe()
d_wa_8 = d_wa_8.iloc[1:8,:]
d_wa_8_flat = d_wa_8.to_numpy().flatten('F')
final_df.iloc[80,:] = d_wa_8_flat


d_wa_9 = wa_9.drop(columns = ['time_wa_9']).describe()
d_wa_9 = d_wa_9.iloc[1:8,:]
d_wa_9_flat = d_wa_9.to_numpy().flatten('F')
final_df.iloc[81,:] = d_wa_9_flat


d_wa_10 = wa_10.drop(columns = ['time_wa_10']).describe()
d_wa_10 = d_wa_10.iloc[1:8,:]
d_wa_10_flat = d_wa_10.to_numpy().flatten('F')
final_df.iloc[82,:] = d_wa_10_flat


d_wa_11 = wa_11.drop(columns = ['time_wa_11']).describe()
d_wa_11 = d_wa_11.iloc[1:8,:]
d_wa_11_flat = d_wa_11.to_numpy().flatten('F')
final_df.iloc[83,:] = d_wa_11_flat


d_wa_12 = wa_12.drop(columns = ['time_wa_12']).describe()
d_wa_12 = d_wa_12.iloc[1:8,:]
d_wa_12_flat = d_wa_12.to_numpy().flatten('F')
final_df.iloc[84,:] = d_wa_12_flat


d_wa_13 = wa_13.drop(columns = ['time_wa_13']).describe()
d_wa_13 = d_wa_13.iloc[1:8,:]
d_wa_13_flat = d_wa_13.to_numpy().flatten('F')
final_df.iloc[85,:] = d_wa_13_flat


d_wa_14 = wa_14.drop(columns = ['time_wa_14']).describe()
d_wa_14 = d_wa_14.iloc[1:8,:]
d_wa_14_flat = d_wa_14.to_numpy().flatten('F')
final_df.iloc[86,:] = d_wa_14_flat



d_wa_15 = wa_15.drop(columns = ['time_wa_15']).describe()
d_wa_15 = d_wa_15.iloc[1:8,:]
d_wa_15_flat = d_wa_15.to_numpy().flatten('F')
final_df.iloc[87,:] = d_wa_15_flat





print(final_df)

final_df.to_csv('Extracted_Whole_Feature.csv')



"""

Extracted_Wholed_Features is a .csv file containing the required data, a summary
of each instance


"""