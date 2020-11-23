import pandas as pd
# create and print a data series
#myseries = pd.Series([439, 98.54, "Hello World", "Sea Breeze", -342])
#print(myseries)

#create and print a data frame
#sales = {"Pie Type": ["Steak and Ale", "Lamb and Mint", "Chicken Balti"],
#         "Key Ingredient": ["Steak", "Lamb", "Chicken"],
#         "Price": [3.00, 3.20, 4.00]}

#sales_frame = pd.DataFrame(sales)

#print(sales_frame)
#importing data from a csv file

vetdata = pd.read_csv("vet_data.csv")

#print(vetdata) #prints all data in file
#[[]] for data frame, [] for series
#print(vetdata[["Pet_Age", "Type", "Chipped", "Pet_Name"]])

#for printing rows (observations)
#print(vetdata[0:4])
#print(vetdata[8:12])

#get rid of unwanted data

vetdata2 = vetdata.drop(["Unnamed: 6", "Unnamed: 7"], axis=1, inplace = False)

#print(vetdata2)

#iloc function pulls out info based on the indexing

print(vetdata2.iloc[7, 4])