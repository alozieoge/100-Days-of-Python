import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data["Primary Fur Color"])

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]

squirrel_count = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
}

# print(squirrel_count)
data_squirrel_count = pd.DataFrame(squirrel_count)
data_squirrel_count.to_csv("squirrel_count.csv")
