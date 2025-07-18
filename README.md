# Squirrel Fur Colour Counter 🐿️

This simple Python project analyses the 2018 Central Park Squirrel Census dataset to count how many squirrels have each **primary fur colour**. It then outputs the result into a new CSV file.

## 📁 Dataset

The dataset used is:  
**2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv**

## 🧠 What It Does

- Reads the squirrel census data using `pandas`
- Counts how many squirrels have each fur colour (e.g. Gray, Cinnamon, Black)
- Stores the results in a clean CSV file: `squirrel.count.csv`

## 🐍 Requirements

- Python 3.x
- pandas

Install pandas if you don't have it:
```bash
pip install pandas