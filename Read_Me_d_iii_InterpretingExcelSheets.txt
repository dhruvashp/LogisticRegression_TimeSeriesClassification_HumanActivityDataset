In each time series, post split, the arrangement for an L for our final features was:

First all the mean of time series, Then standard Deviation and finally Maximum

The L_P Matrix has rows as : 1,1,2,2............20,20

In 1,1 say, the first 1 under columns has the feature index that was selected, in that order. Originally each feature was indexed from 0,1,.....
With constant added for statsmodels the final arrangement was :

constant,0,1.........

The selected indices for features for l=1 is say >> 31,40  (random)

Then 1 will contain 31,40
The second one, right underneath will contain it's p-values

In case for 4,4 and 6,6 multiple features were selected however each had very small p-value and thus don't appear in the Excel Extracted sheed (appeared as NaN in p-value
array)

Thus the final features, in that order, displayed relative to the original whole set, have been displayed for each l against its corresponding p-value


The second sheet contains the predicted y's on the training data, corresponding to these final selected features

THUS
SHEET L_P has features selected and their p values


SHEET Best_Y_Train has best feature y-predicted on these selected features for each L

