import numpy as np
#imports numpy dictionary to programme

a = np.arange(4, 13).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
c = np.row_stack((a, b))
d = np.dot(a, b)
e = np.sum(c)
f = np.sum(c, axis=0)
g = np.sum(c, axis=1)

print("Array A and Array B stacked vertically")
print(c, "\n")
print("Dot calculation of arrays a & b, \n", d)
print("Sum calculation of array a & b stacked into one array, ", e)
print("Sum calculation of columns in array a & b stacked into one array, ", f)
print("Sum calculation of rows in array a & b stacked into one array, ", g)
