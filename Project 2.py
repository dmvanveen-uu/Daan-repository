

# CHANGELOG:

#v1.2 Jeroen added link to google form
#v1.1 Jeroen added parts of the existing code into this file
# v1: Daan created a new import function


#Hello Omar and Jeroen!

# Lets save the data in this format:
# names = [name1, name2, name3]
# tables = [table1, table2, table3, ...]
#  with table1 = [name of person in seat1, name of person in seat2, etc ... ]

# Kind regards, Daan!

# imported from source code
import pandas as pd
import csv
import random
import copy
import os

# Start by presenting the Google form to the user to fill out

print("Welcome to our matching algorithm! To start, you can share this form to fill out by the users.")
print("After filling this form out, please hit enter to receive the link to download the CSV file")
print("https://docs.google.com/forms/d/e/1FAIpQLSd6CeVgLXvRE5YGlkfYEkanezgUMk_-0mmGZOGv39igk2e7Lg/viewform?usp=dialog")

#



##################################################################
########## CODE TO EXTRACT NAMES FROM FILE #######################
##################################################################



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
print(f"These are a total of {len(names)} names entered, these are the names: {names}")





##################################################################
##################################################################
##################################################################



