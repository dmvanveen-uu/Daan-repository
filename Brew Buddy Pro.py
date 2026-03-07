# CHANGELOG:


#v1.6 Jeroen: Grabbed Omar's code and merged it with Project 2.py already on Daan's git repo. 
            # added def display_instructions(): for error handling if .csv is not found. 
            # Put .csv file in {} to make it dynamic..
            # changed name to Brew Buddy Pro (also changed filename on GitHub)
#v1.5 Omar worked on the matching algorithm. See separate file.
#v1.4 Daan replaced old import function with updated version of the existing one + 1 bug fix
#v1.3 Jeroen added instructions to fill out and import the Google Form and CSV file    
#v1.2 Jeroen added link to google form
#v1.1 Jeroen added parts of the existing code into this file
# v1: Daan created a new import function




import pandas as pd
import random
import os


# @daan can you make sure to match this filename below to the output document name from google sheets?
participants_csv = "coffee_form.csv"

# JB: Created a seperate function if .csv file is not loaded correctly with help guide.

def display_instructions():
    
    print("\nWhoops, that didn't work! No worries, we'll guide you through the steps neccesary.")
    print("\nFirst, make sure everyone who wants to participate filled out this form below:")
    print("\nhttps://docs.google.com/forms/d/e/1FAIpQLSd6CeVgLXvRE5YGlkfYEkanezgUMk_-0mmGZOGv39igk2e7Lg/viewform?usp=dialog")

    print("\nThis Google Sheets doc below collected all the data from the Google Form.")
    print("\nhttps://docs.google.com/spreadsheets/d/1PpeRo5NwWtCWgkyHn9dRoUrztqWxIX0mFlPERe4WtIU/edit?usp=sharing")
    print("Now you need to download this spreadsheet ({participants_csv}.csv) to your computer. ")
    print("\nYou can import the .CSV file by:")
    print("\n--> opening the link above in your browser")
    print("\n--> Go to file in the top left corner")
    print("\n--> Go to download")
    print('\n--> select the "seperated by comma\'s" .csv option')
    print("\n--> The file is now downloaded to your computer")
    print("\n--> Make sure the .csv file is in the same directory (folder) as this script")
    print("\n--> Make sure the file name matches {participants_csv}. You might need to change the filename. A typo will result in an error in the script")
    input("\nDone? Press Enter to continue and run the script again.")
    



#####


print("Welcome to Brewbuddy Pro! ")
print("----------------------------------")
print("\n1. Fill in the Google Form")
print("https://docs.google.com/forms/d/e/1FAIpQLSd6CeVgLXvRE5YGlkfYEkanezgUMk_-0mmGZOGv39igk2e7Lg/viewform?usp=dialog")
print("\n2. Download the responses as CSV")
print("https://docs.google.com/spreadsheets/d/1PpeRo5NwWtCWgkyHn9dRoUrztqWxIX0mFlPERe4WtIU/edit?usp=sharing")
print("\n3. Place the CSV file in the same folder as this Python script")
input("\nDone? Press Enter to continue to run the script.")
print("----------------------------------\n")



df = None
while df is None:
    try:
        df = pd.read_csv(participants_csv)
        print(f"Success: Loaded {len(df)} participants from {participants_csv}.")
    except FileNotFoundError:
        print(f"Error: '{participants_csv}' not found.")
        display_instructions()


# show columns (helps debugging)
print("CSV columns:", df.columns)

# extract names and emails
names = list(df["What is your name?"])
emails = list(df["What is your email address?"])

participants = list(zip(names, emails))

print("\nParticipants loaded:", len(participants))

# choose group size
group_size = int(input("Enter group size (2,3,4...): "))

# randomize participants
random.shuffle(participants)

groups = []

# create groups
for i in range(0, len(participants), group_size):
    groups.append(participants[i:i+group_size])

# load conversation starters
if os.path.exists("conversation_starters.txt"):
    with open("conversation_starters.txt", "r") as f:
        starters = f.readlines()
else:
    starters = [
        "What hobby would you start if you had more time?",
        "What is the best coffee you ever had?",
        "If you could travel anywhere tomorrow, where would you go?",
        "What skill would you like to learn this year?"
    ]

starter = random.choice(starters).strip()

print("\nConversation Starter:")
print(starter)

print("\nGenerated Groups:\n")

# print groups
for i, group in enumerate(groups):

    print("Group", i+1)

    for person in group:
        print("-", person[0], "(", person[1], ")")

    print()

# create messages folder if not exists
if not os.path.exists("messages"):
    os.mkdir("messages")

# generate message files
for i, group in enumerate(groups):

    message = "Hello everyone,\n\n"
    message += "You have been matched for Mystery Coffee!\n\n"

    message += "Participants:\n"

    for person in group:
        message += "- " + person[0] + "\n"

    message += "\nConversation starter:\n"
    message += starter + "\n\n"

    message += "Enjoy your coffee meeting!\n"

    file_path = f"messages/group_{i+1}.txt"

    with open(file_path, "w") as f:
        f.write(message)

print("Messages saved in 'messages' folder.")

print("\nMystery Coffee finished successfully!")
