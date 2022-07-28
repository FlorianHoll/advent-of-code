"""Day 1 of Advent of Code without help of packages.

To do this, count the number of times a depth measurement increases from the
previous measurement. (There is no measurement before the first measurement.)
In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?
"""
import numpy as np
import pandas as pd

data = pd.read_csv("../data/day_1_input.txt", header=None)
data = data.values.flatten()
numbers = data.copy()
following_numbers = np.roll(data, -1)
# Note: The last position can be ignored since it is certainly smaller than the first one.
nr_ascending = (following_numbers > numbers).sum()

print(f"Number of measurements larger than previous measurement: {nr_ascending}")
