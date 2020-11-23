import numpy as np

user_name = input("What's your name?")
user_age = input("What's your age?")

np.savetxt("array.txt", np.array([[user_name, ",", user_age]]), fmt="%s")
