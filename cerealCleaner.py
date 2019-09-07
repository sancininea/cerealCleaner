# Cereal cleaner exercise
# We are gonna open a CSV file, read it, and print in screen the cereals with more than 5 grams of fiber

# import librarys
import csv
import os

# Sorce variables
cerealCsv = os.path.join(".","resources","cereal.csv")

# List data


# Open file
with open(cerealCsv, "r", encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)
    print(f"The header is: {csvHeader}")
    # Read all the data and print it if they fullfil the requirements
    for row in csvReader:
     
        if float(row[7]) > 5:
            print(row)
