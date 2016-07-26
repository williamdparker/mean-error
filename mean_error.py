#!/usr/bin/env python

import numpy as np

baseline_data = np.array([1, 2, 3])
test_data = np.array([1.1, 1.9, 3])

difference = test_data - baseline_data
absolute_difference = abs(test_data - baseline_data)
relative_difference = difference / abs(baseline_data)
absolute_relative_difference = absolute_difference / abs(baseline_data)
#print "{}".format(difference)
#print "{}".format(absolute_difference)
#print "{}".format(relative_difference)
#print "{}".format(absolute_relative_difference)

me = np.mean(difference, dtype=np.float64)
mae = np.mean(absolute_difference, dtype=np.float64)
mre = np.mean(relative_difference, dtype=np.float64)
mare = np.mean(absolute_relative_difference, dtype=np.float64)

print "Baseline Data = {}".format(baseline_data)
print "Comparison Data = {}".format(test_data)
print "ME = {}".format(me)
print "MAE = {}".format(mae)
print "MRE = {}".format(mre)
print "MARE = {}".format(mare)
