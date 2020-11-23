import numpy as np
# applies numpy dictionary to programme

a = np.ones(9)
#1 = true in boolean
b = a.reshape(3, 3)
#creates 3x3 array
c = b.astype(bool)
# converts int to boolean

print(c)