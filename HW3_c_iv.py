# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 08:47:51 2020

@author: DHRUV
"""


"""

HW3 (c) (iv)

Having obtained the confidence range standard deviations for each of the 42 features over
our entire dataset, we can say the following:
    
Over different instances, belonging to different classes, if the variation in a feature
is not a lot, then that feature won't be able to carefully discriminate between different
classes on the test set.

Thus over the same class, a feature that varies low is preferred, but over different classes
we need features that vary, so that we can distinguish between different classes using those
features.

Our standard deviation calculation was over all classes, for each feature, and thus if one wants
to select features based on this standard deviation calculation, it would be most fruitful
to select features that have some standard deviation. If the standard deviation is low
over all classes of a feature it implies that over the entire class range that feature doesn't
vary too much and thus doesn't have the characteristics of class distinguishability. Thus
we'll select features that have standard deviations which are noticeable.

    
The option given in the HW3 PDF is max, min and mean and observing these values over all features
(3*6 = 18), we see that they do have a decent enough standard deviation and thus can
distinguish well between classes.

Once could go with any other alternate approach that makes sure that the features selected 
have a decent enough standard deviation.

Standard deviations can't be compared for different features with different means that well, as
0.01 and 0.05 are just as distinguishable as 1 and 5, but 1 and 5 has a higher standard deviation
than 0.01 and 0.05. So we have to gauge a 'large value of standard deviation' as 'large', by comparing
the value of the standard deviation of a feature against its mean. The farther it is from its mean,
more we have a distinguishing factor for the system. Scales don't affect this discussion much
unless our algorithm is run on a system that has major rounding up issues. 

Thus we need to gauge standard deviations versus their mean, higher deviations compared to 
their means give us better features in terms of distinguishability. Again while a good 'generic metric',
it may not always be possible for us to gauge feature distinctness in different classes just
by looking at the standard deviations and means, but it is a usable metric.

Other than standard deviation, glancing through our data, we can select those features that
have a tendency of changing over different classes. This is obviously possible here as our
data set only has 88 rows. There are a few alternatives to selecting our features.

We could go with min, max, q1

Or even median, max, q1 (multiple such triplets can be selected on the preceding standard deviation
criteria)

We'll go with :

max, mean, standard deviation


as observing values of min we see that they are consistently 0 over classes

"""