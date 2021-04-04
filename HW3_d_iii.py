# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 04:51:38 2020

@author: DHRUV
"""


"""
HW3_d_iii
"""

"""
Assumptions
Once the time series have been split we will use
Mean, Standard Deviation and Max for every single resultant time series in general

Various Matrices will be formed for our outputs which will be explained in the
comments section as they are formed

"""

import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm 

"""
Reading the train data
"""

df1 = pd.read_csv('bending1\\training\\dataset3.csv')
df2 = pd.read_csv('bending1\\training\\dataset4.csv')
df3 = pd.read_csv('bending1\\training\\dataset5.csv')
df4 = pd.read_csv('bending1\\training\\dataset6.csv')
df5 = pd.read_csv('bending1\\training\\dataset7.csv')




df6 = pd.read_csv('bending2\\training\\dataset3.csv')
df7 = pd.read_csv('bending2\\training\\dataset4.csv')
df8 = pd.read_csv('bending2\\training\\dataset5.csv')
df9 = pd.read_csv('bending2\\training\\dataset6.csv')
 



df10 = pd.read_csv('cycling\\training\\dataset4.csv')
df11 = pd.read_csv('cycling\\training\\dataset5.csv')
df12 = pd.read_csv('cycling\\training\\dataset6.csv')
df13 = pd.read_csv('cycling\\training\\dataset7.csv')
df14 = pd.read_csv('cycling\\training\\dataset8.csv')
df15 = pd.read_csv('cycling\\training\\dataset9.csv')
df16 = pd.read_csv('cycling\\training\\dataset10.csv')
df17 = pd.read_csv('cycling\\training\\dataset11.csv')
df18 = pd.read_csv('cycling\\training\\dataset12.csv')
df19 = pd.read_csv('cycling\\training\\dataset13.csv')
df20 = pd.read_csv('cycling\\training\\dataset14.csv')
df21 = pd.read_csv('cycling\\training\\dataset15.csv')






df22 = pd.read_csv('lying\\training\\dataset4.csv')
df23 = pd.read_csv('lying\\training\\dataset5.csv')
df24 = pd.read_csv('lying\\training\\dataset6.csv')
df25 = pd.read_csv('lying\\training\\dataset7.csv')
df26 = pd.read_csv('lying\\training\\dataset8.csv')
df27 = pd.read_csv('lying\\training\\dataset9.csv')
df28 = pd.read_csv('lying\\training\\dataset10.csv')
df29 = pd.read_csv('lying\\training\\dataset11.csv')
df30 = pd.read_csv('lying\\training\\dataset12.csv')
df31 = pd.read_csv('lying\\training\\dataset13.csv')
df32 = pd.read_csv('lying\\training\\dataset14.csv')
df33 = pd.read_csv('lying\\training\\dataset15.csv')






    
df34 = pd.read_csv('sitting\\training\\dataset4.csv')
df35 = pd.read_csv('sitting\\training\\dataset5.csv')
df36 = pd.read_csv('sitting\\training\\dataset6.csv')
df37 = pd.read_csv('sitting\\training\\dataset7.csv')
df38 = pd.read_csv('sitting\\training\\dataset8.csv')
df39 = pd.read_csv('sitting\\training\\dataset9.csv')
df40 = pd.read_csv('sitting\\training\\dataset10.csv')
df41 = pd.read_csv('sitting\\training\\dataset11.csv')
df42 = pd.read_csv('sitting\\training\\dataset12.csv')
df43 = pd.read_csv('sitting\\training\\dataset13.csv')
df44 = pd.read_csv('sitting\\training\\dataset14.csv')
df45 = pd.read_csv('sitting\\training\\dataset15.csv')







df46 = pd.read_csv('standing\\training\\dataset4.csv')
df47 = pd.read_csv('standing\\training\\dataset5.csv')
df48 = pd.read_csv('standing\\training\\dataset6.csv')
df49 = pd.read_csv('standing\\training\\dataset7.csv')
df50 = pd.read_csv('standing\\training\\dataset8.csv')
df51 = pd.read_csv('standing\\training\\dataset9.csv')
df52 = pd.read_csv('standing\\training\\dataset10.csv')
df53 = pd.read_csv('standing\\training\\dataset11.csv')
df54 = pd.read_csv('standing\\training\\dataset12.csv')
df55 = pd.read_csv('standing\\training\\dataset13.csv')
df56 = pd.read_csv('standing\\training\\dataset14.csv')
df57 = pd.read_csv('standing\\training\\dataset15.csv')










df58 = pd.read_csv('walking\\training\\dataset4.csv')
df59 = pd.read_csv('walking\\training\\dataset5.csv')
df60 = pd.read_csv('walking\\training\\dataset6.csv')
df61 = pd.read_csv('walking\\training\\dataset7.csv')
df62 = pd.read_csv('walking\\training\\dataset8.csv')
df63 = pd.read_csv('walking\\training\\dataset9.csv')
df64 = pd.read_csv('walking\\training\\dataset10.csv')
df65 = pd.read_csv('walking\\training\\dataset11.csv')
df66 = pd.read_csv('walking\\training\\dataset12.csv')
df67 = pd.read_csv('walking\\training\\dataset13.csv')
df68 = pd.read_csv('walking\\training\\dataset14.csv')
df69 = pd.read_csv('walking\\training\\dataset15.csv')






df1 = df1.drop(df1.columns[0],axis=1)
df2 = df2.drop(df2.columns[0],axis=1)
df3 = df3.drop(df3.columns[0],axis=1)
df4 = df4.drop(df4.columns[0],axis=1)
df5 = df5.drop(df5.columns[0],axis=1)
df6 = df6.drop(df6.columns[0],axis=1)
df7 = df7.drop(df7.columns[0],axis=1)
df8 = df8.drop(df8.columns[0],axis=1)
df9 = df9.drop(df9.columns[0],axis=1)
df10 = df10.drop(df10.columns[0],axis=1)
df11 = df11.drop(df11.columns[0],axis=1)
df12 = df12.drop(df12.columns[0],axis=1)
df13 = df13.drop(df13.columns[0],axis=1)
df14 = df14.drop(df14.columns[0],axis=1)
df15 = df15.drop(df15.columns[0],axis=1)
df16 = df16.drop(df16.columns[0],axis=1)
df17 = df17.drop(df17.columns[0],axis=1)
df18 = df18.drop(df18.columns[0],axis=1)
df19 = df19.drop(df19.columns[0],axis=1)
df20 = df20.drop(df20.columns[0],axis=1)
df21 = df21.drop(df21.columns[0],axis=1)
df22 = df22.drop(df22.columns[0],axis=1)
df23 = df23.drop(df23.columns[0],axis=1)
df24 = df24.drop(df24.columns[0],axis=1)
df25 = df25.drop(df25.columns[0],axis=1)
df26 = df26.drop(df26.columns[0],axis=1)
df27 = df27.drop(df27.columns[0],axis=1)
df28 = df28.drop(df28.columns[0],axis=1)
df29 = df29.drop(df29.columns[0],axis=1)
df30 = df30.drop(df30.columns[0],axis=1)
df31 = df31.drop(df31.columns[0],axis=1)
df32 = df32.drop(df32.columns[0],axis=1)
df33 = df33.drop(df33.columns[0],axis=1)
df34 = df34.drop(df34.columns[0],axis=1)
df35 = df35.drop(df35.columns[0],axis=1)
df36 = df36.drop(df36.columns[0],axis=1)
df37 = df37.drop(df37.columns[0],axis=1)
df38 = df38.drop(df38.columns[0],axis=1)
df39 = df39.drop(df39.columns[0],axis=1)
df40 = df40.drop(df40.columns[0],axis=1)
df41 = df41.drop(df41.columns[0],axis=1)
df42 = df42.drop(df42.columns[0],axis=1)
df43 = df43.drop(df43.columns[0],axis=1)
df44 = df44.drop(df44.columns[0],axis=1)
df45 = df45.drop(df45.columns[0],axis=1)
df46 = df46.drop(df46.columns[0],axis=1)
df47 = df47.drop(df47.columns[0],axis=1)
df48 = df48.drop(df48.columns[0],axis=1)
df49 = df49.drop(df49.columns[0],axis=1)
df50 = df50.drop(df50.columns[0],axis=1)
df51 = df51.drop(df51.columns[0],axis=1)
df52 = df52.drop(df52.columns[0],axis=1)
df53 = df53.drop(df53.columns[0],axis=1)
df54 = df54.drop(df54.columns[0],axis=1)
df55 = df55.drop(df55.columns[0],axis=1)
df56 = df56.drop(df56.columns[0],axis=1)
df57 = df57.drop(df57.columns[0],axis=1)
df58 = df58.drop(df58.columns[0],axis=1)
df59 = df59.drop(df59.columns[0],axis=1)
df60 = df60.drop(df60.columns[0],axis=1)
df61 = df61.drop(df61.columns[0],axis=1)
df62 = df62.drop(df62.columns[0],axis=1)
df63 = df63.drop(df63.columns[0],axis=1)
df64 = df64.drop(df64.columns[0],axis=1)
df65 = df65.drop(df65.columns[0],axis=1)
df66 = df66.drop(df66.columns[0],axis=1)
df67 = df67.drop(df67.columns[0],axis=1)
df68 = df68.drop(df68.columns[0],axis=1)
df69 = df69.drop(df69.columns[0],axis=1)






df_list = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50,df51,df52,df53,df54,df55,df56,df57,df58,df59,df60,df61,df62,df63,df64,df65,df66,df67,df68,df69]

out = np.zeros(69)

for z in np.arange(0,9):
    out[z] = 1



y = pd.DataFrame(out)



l = np.arange(1,21)
datalist = np.arange(0,69)
l_new = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
l_p = pd.DataFrame(index=l_new,columns=np.arange(0, 18*20+1))
best_train_fit = pd.DataFrame(index=datalist,columns=l)

#In the above deliberation l_p contains the l,p value matrix. Since we have maximum 20 splits, maximum time series = 120, each of the 120 will have three features, so 360 total features. These features each will have an associated p value in addition to p value of the constant. So maximum p values are 361 stored in index from 0 to 360. As np.arange excludes the end value, we have kept the end at 361. The p-value's for lesser splits will be fewer and those values in the matrix will stay NaN
#Best train fit is a 69*20 matrix, where each column corresponds to an l, and contains the y_predicted for best fit for that l obtained via RFE


for i in l:
    splits = np.arange(0,i)
    segment = math.floor(480/i)
    df_list_new = []
    j = 0
    for j in datalist:
        list_df_specific = []
        df_parts = 0
        for df_parts in splits:
             list_df_specific.append(df_list[j].iloc[((df_parts)*(segment)) : ((df_parts + 1)*(segment)),:].reset_index(drop=True))
        df_list_new.append(pd.concat(list_df_specific, axis=1))
    
    header_column = np.arange(0, 18*i) 
    features = pd.DataFrame(index=datalist,columns=header_column) 
   

    
#The above code has split the time series and stored the split time series instances in the
#list df_list_new for a value of l

#Now we extract features before fitting the data. Our features will be, for each time series, mean,
#standard deviation and max as it had been in previous parts of the question

#The features will appear as thus in the final matrix of features -
#First we will have all the means, then all the standard deviations and finally maximum values
#Thus mean of all timeseries, then standard deviation of all timeseries and finally maximum values of all time series

    t=0
    for t in datalist:
        features.iloc[t, 0 : (6*i)]       =    (((pd.DataFrame(df_list_new[t].mean()).transpose()).to_numpy()).flatten())[:]
        features.iloc[t, (6*i) : (12*i)]  =    (((pd.DataFrame(df_list_new[t].std()).transpose()).to_numpy()).flatten())[:]
        features.iloc[t, (12*i) : (18*i)] =    (((pd.DataFrame(df_list_new[t].max()).transpose()).to_numpy()).flatten())[:]
    
    X = sm.add_constant(features)
    model = sm.Logit(y,X.astype(float))
    fit = model.fit(maxiter=10)
    results_summary = fit.summary()
    
    results_as_html = results_summary.tables[1].as_html()
    summ = pd.read_html(results_as_html, header=0, index_col=0)[0]
    p_interim = summ['P>|z|']
    p = (p_interim.to_numpy()).astype(float)
    
    
#Lines 265 and 266 referenced from https://stackoverflow.com/questions/51734180/converting-statsmodels-summary-object-to-pandas-dataframe
#This code calculates collects p values from summary table into a dataframe, summ, from which p values are stored in a numpy array for RFE
    
#Total p values for this l = i will be, 18*i + 1 (1 for the constant), collected from constant to all the features in a consequential order
#indexing of these p in numpy will be from 0 to 18*i 
#in statsmodels prediction gives probability of being 1, thus if that is >= 0.5, it'll be made 1, otherwise 0
#index for l_p is from 1 to 20 (l) and header for best_train_fit is from 1 to 20 (l), however iloc uses pandas internal dataframe values for indexing from 0 to 19. So storing in entities for an l = i corresponds to storing in index i-1 for the dataframes as such 


    
    if np.all(p <= 0.05):
        header = X.columns
        l_p.iloc[2*i - 2,0:np.size(header)] = header[:]
        l_p.iloc[2*i - 1,0:np.size(p)] = p[:]
        y_predicted = ((fit.predict(X)) >= 0.5).astype(int)
        best_train_fit.iloc[:,i-1] = y_predicted[:]
        print('For the split : \n',i)
        print('The final p-values for unmodified (does not need modification) feature set is : \n',p)
        
    
    else:
        
        while np.any(p > 0.05):
            
            redact = np.argmax(p)
            X.drop(X.columns[redact],axis=1,inplace = True)
           
            model_RFE = sm.Logit(y,X.astype(float))
            fit_RFE = model_RFE.fit(maxiter=10)
            results_summary = fit_RFE.summary()
                
            results_as_html = results_summary.tables[1].as_html()
            summ = pd.read_html(results_as_html, header=0, index_col=0)[0]
            p_interim = summ['P>|z|']
            p = (p_interim.to_numpy()).astype(float)
        
# We have the updated feature set X, corresponding p values, the selected features in X's column headers. The p-value correspond to those features        
# model_RFE contains the model with the modified X features that terminated the while loop with p values <=0.05        
       
            
        header = X.columns
        l_p.iloc[2*i - 2,0:np.size(header)] = header[:]
        l_p.iloc[2*i - 1,0:np.size(p)] = p[:]
        y_predicted_RFE = ((fit_RFE.predict(X)) >= 0.5).astype(int)
        best_train_fit.iloc[:,i-1] = y_predicted_RFE[:]
        print('For the split : \n',i)
        print('The final p-values for modified (needs modification) feature set is : \n',p)
        
        if(i==4):
            p_4 = p
        
        
            
       
# Above code removes feature recursively with the highest p value one by one till all p values are <= 0.05. Once they are <=0.05 the while loop ends  
    

l_p.to_csv('L_and_P_matrix_d_iii.csv')
best_train_fit.to_csv('Best_Y_Predicted_On_Train_d_iii.csv')


print('The p_4 is : \n', p_4)    

#p_4 had nan as the summary sheet it was taken from didn't display it due to p being extremely small
#However the recursion worked as features were extracted for l=4 splits too in general
print('The l and p matrix is : \n', l_p)
print('The best train fit matrix for each different value of l corresponding to best feature set is : \n', best_train_fit)
    
    
    
    

    
    
    
    
    
