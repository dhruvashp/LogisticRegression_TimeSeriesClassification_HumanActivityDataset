As such, again, we have
optimal l around 2-3  
So optimal splits appear about l=2 or l=3 
There is another l that gives a low error around l=15
But since l=2 or l=3 was common in p-value recursion, we will go with those
values

Additionally number of features can be seen from the excel sheet corresponding
to feature, coefficient matrix

As such this matrix is sparse, and where it had NaN's during python run,
the corresponding features didn't exist and thus displayed NaN

This was because for each l the number of features are different

Of all possible features for our split, they have been numbered correspondingly
and beneath them in the matrix we have their values

This matrix is more or less lower triangular, and even in the
lower triangular portion is sparse, as of all possible features
for a given split, the features actually relevant or non-zero
were even fewer

for l=2 or l=3 features selected are around 8-9 
for both these l's with low errors, the intercept coefficient was penalized
to 0

once could easily add codes to count zeros in the matrix and the minimum
error index in the error vector and give those finalized outputs
however in a sense of total examination, I haven't done that, and I've
assumed that once the relevant matrices and vectors have been obtained
feature selection is left for the individual to deliberate with

result corresponding to l=15 hasn't been shown and can be cross-referenced
from the matrix easily

mapping of feature index to actual time-series features can be done
exactly as it was done before
OR
one could forgo those original 'time-series' headers and work
with headers as obtained post data combination for different splits
in python itself