import pandas as pd
#import pies.csv file
pieList = pd.read_csv("pies.csv")
#replace the index with the correct SKU format
pieList.index = ["SKU000001", "SKU000002", "SKU000003", "SKU000004", "SKU000005", "SKU000006", "SKU000007", "SKU000008"]
print(pieList)
#drop the SKU column as the index serves in it's place
pieList1 = pieList.drop(["SKU"], axis=1, inplace = False)
print(pieList1)
#print just the pie type column
print(pieList1["Pie Type"])
#print both the pie type and price columns
print(pieList1[["Pie Type", "Price"]])
#print observations 4-7
print(pieList1[3:7])
#print observation 7
print(pieList1.iloc[6])

#set the column for observations to be checked against
pieList2= pd.read_csv("pies.csv", index_col="Main Ingredient")
#print observations where main ingredient = chicken
print(pieList2.loc["Chicken"])
#print observations where main ingredient = chicken or steak
print(pieList2.loc[["Chicken", "Steak"]])

#print observations 4-7, columns 2-4
print(pieList2.iloc[3:7, 2:4])