import pandas as pd

# read the CSV file
data = pd.read_csv("data.csv")

# extract relevant information
name = data["Name"].values[0]
email = data["Email"].values[0]
phone = data["Phone"].values[0]
