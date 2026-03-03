print("Hello world!")

#Hello Omar and Jeroen!

# Lets save the data in this format:
# names = [name1, name2, name3]
# tables = [table1, table2, table3, ...]
#  with table1 = [name of person in seat1, name of person in seat2, etc ... ]

# Kind regards, Daan!


##################################################################
########## CODE TO EXTRACT NAMES FROM FILE #######################
##################################################################

import csv

# get name of file, add .csv if the user hasn't
filename = "coffee_form.csv"
filename = input("What is the name of the csv file? ")
if not filename[len(filename)-4:] == ".csv":
    filename += ".csv"

# open file and prep for reading the file
print(f"Now opening {filename}.")
openfile = open(filename, newline='')
csvreader = csv.reader(openfile)

#read all rows of the file and add the 2nd item (the name) to a list
print("Now saving all the names from the file into a list.")
names = []
firstrow = True
for row in csvreader:
    #skip the first row, because that just contains the question
    if firstrow:
        firstrow = False
        continue
    names.append(row[1])
print(f"These are the names entered: {names}")




