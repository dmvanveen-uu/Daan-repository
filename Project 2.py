

# CHANGELOG:

#v1.4 Daan replaced old import function with updated version of the existing one + 1 bug fix
#v1.3 Jeroen added instructions to fill out and import the Google Form and CSV file    
#v1.2 Jeroen added link to google form
#v1.1 Jeroen added parts of the existing code into this file
# v1: Daan created a new import function


# imported from source code
import pandas as pd
import csv
import random
import copy
import os

# Start by presenting the Google form to the user to fill out

print("Welcome to our matching algorithm! To start, you can share this form to fill out by the users.")
print("https://docs.google.com/forms/d/e/1FAIpQLSd6CeVgLXvRE5YGlkfYEkanezgUMk_-0mmGZOGv39igk2e7Lg/viewform?usp=dialog")
print("After filling this form out, please hit enter to receive the link to download the CSV file")

print("This Google Sheets doc below collected all the data from the Google Sheets mentioned above")
print("You can import the .CSV file by:")
print(" --> opening the link below")
print("--> Go to file in the top left corner")
print("--> Go to download")
print('--> select the "seperated by comma\'s" .csv option')
print("--> The file is now downloaded to your computer")
print("--> Make sure the .csv file is in the same directory (folder) as this script")
print("! Remember the file name, you will be asked to input the filename later in this script. A typo will result in an error in the script")

print("https://docs.google.com/spreadsheets/d/1PpeRo5NwWtCWgkyHn9dRoUrztqWxIX0mFlPERe4WtIU/edit?usp=sharing")

DELIMITER=','


# get name of participant info file, add '.csv' if the user hasn't
participants_csv = "coffee_form.csv"
temp = input("What is the name of the csv file? ")
if not temp == "":
    participants_csv = temp
if not participants_csv[len(participants_csv)-4:] == ".csv":
    participants_csv += ".csv"

# path to TXT file that stores the pairings of this round
new_pairs_txt = "Coffee Partner Lottery new pairs.txt"

# path to CSV file that stores the pairings of this round
new_pairs_csv = "Coffee Partner Lottery new pairs.csv"

# path to CSV file that stores all pairings (to avoid repetition)
all_pairs_csv = "Coffee Partner Lottery all pairs.csv"

# load participant's data
formdata = pd.read_csv(participants_csv, sep=DELIMITER)
print(pd.DataFrame(formdata))
names = formdata[['What is your email address?']]
print(names)


