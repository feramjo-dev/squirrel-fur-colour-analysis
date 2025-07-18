import pandas

# Read the csv file
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# count fur colours
squirrel_fur_colours_count = squirrel_data["Primary Fur Color"].value_counts()
# print(squirrel_fur_colours_count)

# Convert to DataFrame
squirrel_fur_colours_count_dataframe = squirrel_fur_colours_count.reset_index()
squirrel_fur_colours_count_dataframe.columns = ["Fur Colour", "Count"]


# Export to CSV
squirrel_fur_colours_count_dataframe.to_csv("squirrel.count.csv", index=False)


