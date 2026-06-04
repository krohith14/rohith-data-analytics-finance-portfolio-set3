# Python Pandas Data Analyzer
# Simple Student Version

import pandas as pd

# Function to calculate profit
def calculate_profit(price, cost):
    return price - cost

# Financial data
data = {
    "Stock": ["Tata", "Reliance", "Infosys"],
    "Cost": [1000, 1500, 2000],
    "Price": [1200, 1800, 2300]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Financial Data")
print(df)

print("\nStock Analysis")

for i in range(len(df)):

    stock = df["Stock"][i]
    cost = df["Cost"][i]
    price = df["Price"][i]

    profit = calculate_profit(price, cost)

    print(stock)
    print("Cost:", cost)
    print("Price:", price)
    print("Profit:", profit)

    if profit > 0:
        print("Decision: Profit")
    else:
        print("Decision: Loss")

    print()

# Dictionary for energy readings
energyData = {
    "Day1": 450,
    "Day2": 520,
    "Day3": 480
}

print("Energy Analysis")

for day, reading in energyData.items():

    print(day, "=", reading, "kWh")

    if reading > 500:
        print("High Energy Usage")
    else:
        print("Normal Energy Usage")

# File handling
file = open("report.txt", "w")

file.write("Financial and Energy Analysis Completed")

file.close()

print("\nReport saved in report.txt")