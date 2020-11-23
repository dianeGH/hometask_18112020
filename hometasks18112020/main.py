import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("holidays.csv")
#data sorted for graphical representations
sorted_data = data.sort_values(by=["feedback_score"], ascending=False)
#1.How many rows and columns are there in your file?
print(data.shape)
#2.Print rows 3-8 ( using  iloc/loc).
print(data.iloc[2:8])
#3.Find the mean number of all-inclusive hotels across all destinations.
print(data["all_inclusive_hotels"].mean())
#4.Find the lowest scoring destination
print(data["feedback_score"].min())
#5.Find the highest scoring destination.
print(data["feedback_score"].max())
#6.find all the destinations where there are more than 9 all-inclusive hotels.
print(data[(data.all_inclusive_hotels > 9)])
#7. Filter the data by destination and score above 8.
print(data[(data.feedback_score > 8)])
#8. Filter the data by destination and score below 2
print(data[(data.feedback_score < 2)])
#correlation graph
y = sorted_data["feedback_score"]*10
x = sorted_data["Destination"]

plt.plot(x, y, label="feedback score")

y2 = sorted_data["all_inclusive_hotels"]
x2 = sorted_data["Destination"]

plt.plot(x2, y2, label="all inclusive hotels")

plt.ylabel('numbers')
plt.xlabel('Destination')
plt.title('Correlations')
plt.legend()
plt.show()


#highest scoring destination graph
maximum = sorted_data.iloc[1:6]
print(maximum)
destinations = maximum['Destination']
slices = maximum['feedback_score']
colors = ['r', 'y', 'g', 'b', 'm']

plt.pie(slices, labels=destinations, colors=colors, startangle=90, shadow=True, explode=(0, 0, 0, 0, 0),
        radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.show()
