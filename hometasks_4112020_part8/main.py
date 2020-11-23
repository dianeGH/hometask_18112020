#In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) – remove all repeating  items present in array b
import numpy as np
#importing numpy as programme dictionary

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8, 9])

# concatenate the two arrays, remove non unique characters and the print the array
c = np.concatenate((a, b), axis=0)
d = np.unique(c)
print(d)
