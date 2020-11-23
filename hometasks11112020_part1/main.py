import pandas as pd

movieData = pd.read_csv("Movie-Data.csv", index_col="Director")
print(movieData.loc[["Ridley Scott", "Tom Ford"]])

movieData1 = pd.read_csv("Movie-Data.csv", index_col="Year")
print(movieData1.loc[[2014]])

movieData2 = pd.read_csv("Movie-Data.csv")
print(movieData2.iloc[0:10])