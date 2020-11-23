#A motorbike costs £2000 and loses 10% of its value every year. Using a loop, print the value of the bike every following year until it falls below £1000.
print("Today, Jim bought a motorbike for £2000.00")
year = 1
cost = 2000

while cost >1000:
    print("At the end of year ",year,", Jim's bike is worth £", cost)
    year+=1
    cost=cost*.9