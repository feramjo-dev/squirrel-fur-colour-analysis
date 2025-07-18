import pandas

# Read the csv file
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# count fur colours
squirrel_fur_colours_count = squirrel_data["Primary Fur Color"].value_counts()
# print(squirrel_fur_colours_count)

available_squirrel_colours = []
squirrel_fur_colours_count_list = []
for color, count in squirrel_fur_colours_count.items():
    available_squirrel_colours.append(color)
    squirrel_fur_colours_count_list.append(count)

# creating a dictionary from the "squirrel_fur_colours_count" series
squirrel_fur_colours_count_dict = {
    "Fur Colour": available_squirrel_colours,
    "Count": squirrel_fur_colours_count_list
}

# convert the dictionary to a dataframe and create the csv file
squirrel_fur_colours_count_dataframe = pandas.DataFrame(squirrel_fur_colours_count_dict)
squirrel_fur_colours_count_dataframe.to_csv("squirrel.count.csv")

