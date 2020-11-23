import pandas as pd
data = pd.read_csv("ign.csv")
print(data.shape) # how may rows and columns
print(data.head(3)) #prints the first (number) of rows () auto retireves 5 rows
print(data.tail(4)) #prints the last (number) of rows as above for auto number
print(data["platform"])
print(data["score"].mean()) # mean of the column
print(data.mean()) #mean of all columns
print(data["score"]/2) #divides each item in column
print(data["score"]*10)
print(data.describe()) #gives statistical data for the table
#applies a boolean test against data in the column specified
myfilter= data["score"]>8
print(myfilter)
#selecting rows where the boolean test returns true
highscore = data[myfilter]
print(highscore.head())
#using multiple conditions to filter
print(data[(data.score > 8) & (data.platform == "iPad")])