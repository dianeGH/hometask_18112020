import numpy as np

#array1 = np.ones(18)

#print(array1)

a = np.ones(3)
b = np.ones(3)+1
c = np.ones(3)+2
d = np.arange(1, 4, 1)

e = np.concatenate ((a,b, c, d, d, d),axis=0) #Concatenates arrays
print(e)
