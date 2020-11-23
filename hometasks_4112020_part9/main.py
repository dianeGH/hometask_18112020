#Get all integers between 5 and 10 from arrays a and b and sum them together

import numpy as np
#importing numpy as programme dictionary

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8, 9])

# concatenate the two arrays, remove non unique characters and the print the array
c = np.concatenate((a, b), axis=0)

#sum of the integers greater than or equal to 5 in the array
d = sum(c[c>=5])

print(d)