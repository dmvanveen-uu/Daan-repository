# CHANGELOG:

#v2.1 Jeroen: Added a thank you message and a link to the google sheet responses as a reminder to clear the Google Sheets.
#v2 Daan: Added error handling for input group_size and input rounds. I think its time to commit to v2!
#v1.11 Daan: combined seperate branch made by omar with this one + little bugfix
#v1.10 Daan: fixed a IndentationError
#v1.9 Jeroen: Added a reminder to clear the google sheet responses after the script is run.
#v1.8 Daan: Making sure to match the filename to the output document name from google sheets, with user input as a backup
#v1.7 Jeroen: Added a function (append/pop) to make the residual group more balanced. 
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



participants_csv = "coffeee.csv"
new_pairs_csv = "new_pairs.csv"
all_pairs_csv = "all_pairs.csv"

DELIMITER = ";"


# JB: Created a seperate function if .csv file is not loaded correctly with help guide.
def display_instructions():
    print("\nCSV file not found.")
    print("Follow these steps:")
    print("1. Fill in the Google Form")
    print("2. Download the responses as CSV")
    print("3. Place the CSV file in the same folder as this script")
    input("\nPress Enter when ready...")


print("Welcome to BrewBuddy Pro")
print("----------------------------------")
print("1. Let participants fill in the Google Form\n    (https://docs.google.com/forms/d/e/1FAIpQLSd6CeVgLXvRE5YGlkfYEkanezgUMk_-0mmGZOGv39igk2e7Lg/viewform?usp=dialog)")
print("2. Download the responses as CSV\n    (https://docs.google.com/spreadsheets/d/1PpeRo5NwWtCWgkyHn9dRoUrztqWxIX0mFlPERe4WtIU/edit?usp=sharing)")
print("3. Place the CSV file in this folder")
input("\nPress Enter to continue...")
print("----------------------------------\n")

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



#making sure to match the filename to the output document name from google sheets, with user input as a backup
participants_csv = "coffee_form.csv"
df = None
while df is None:
    try:
        df = pd.read_csv(participants_csv)
        print(f"Success: Loaded {len(df)} participants from {participants_csv}.")
    except FileNotFoundError:
        participants_csv = "Project 2_ Brew Buddy! (Responses) - Formulierreacties 1.csv"
        try:
            df = pd.read_csv(participants_csv)
            print(f"Success: Loaded {len(df)} participants from {participants_csv}.")
        except FileNotFoundError:
            participants_csv = "Project 2_ Brew Buddy! (Responses) - Scores.csv"
            try:
                df = pd.read_csv(participants_csv)
                print(f"Success: Loaded {len(df)} participants from {participants_csv}.")
            except FileNotFoundError:
                #standard names not working, asking the user
                print("Error: File not found.")
                participants_csv = input("How did you name the .csv file? ")
                try:
                    df = pd.read_csv(participants_csv)
                    print(f"Success: Loaded {len(df)} participants from {participants_csv}.")
                except FileNotFoundError:
                    participants_csv = participants_csv + ".csv"
                    try:
                        df = pd.read_csv(participants_csv)
                        print(f"Success: Loaded {len(df)} participants from {participants_csv}.")
                    except FileNotFoundError:
                        print(f"Error: '{participants_csv}' not found.")
                        display_instructions()
print()



# Extract data
names = list(df["What is your name?"])
emails = list(df["What is your email address?"])

participants = list(zip(names, emails))

print("Participants:", len(participants))


# choose group size and number of rounds
group_size = 0
rounds = 0
while not group_size > 0:
    try:
        group_size = int(input("Enter group size (2,3,4...): "))
    except:
        print("Something went wrong with your input, try again.")
while not rounds > 0:
    try:
        rounds = int(input("How many rounds should be generated (2,3,4...): "))
    except:
        print("Something went wrong with your input, try again.")



# assemble output for printout
output_string = ""
output_string += "------------------------\n"
output_string += "Generated coffee groups:\n"
output_string += "------------------------\n"


# load previous pair history
opairs = set()

if os.path.exists(all_pairs_csv):
    with open(all_pairs_csv, "r") as file:
        for line in file:
            opairs.add(tuple(sorted(line.strip().split(DELIMITER))))


# open new pairs csv
with open(new_pairs_csv, "w") as file:

    header = ["round", "group", "name", "email"]
    file.write(DELIMITER.join(header) + "\n")

    for r in range(1, rounds + 1):

        random.shuffle(participants)

        groups = []

        # create groups
        for i in range(0, len(participants), group_size):
            groups.append(participants[i:i+group_size])

        output_string += f"\nRound {r}"
        
        starter = random.choice(starters).strip()
        output_string += f"\nConversation Starter: {starter}\n\n"


        for g in range(len(groups)):

            group = groups[g]

            output_string += f"Group {g+1}: "

            emails_in_group = []

            for person in group:

                name = person[0]
                email = person[1]

                emails_in_group.append(email)

                output_string += f"{name} ({email}) "

                # write row to CSV
                file.write(f"{r}{DELIMITER}{g+1}{DELIMITER}{name}{DELIMITER}{email}\n")

            output_string += "\n"

            # store pair history
            pair_key = tuple(sorted(emails_in_group))

            if pair_key not in opairs:
                opairs.add(pair_key)


# write output to console
print(output_string)


# append history file
mode = "w"


with open(all_pairs_csv, mode) as file:

    for pair in opairs:

        for i in range(len(pair)):

            if i < len(pair) - 1:
                file.write(pair[i] + DELIMITER)
            else:
                file.write(pair[i] + "\n")


print("\nPairings saved successfully.")
print("New pairs file:", new_pairs_csv)
print("History file:", all_pairs_csv)
print("\nProgram finished.")
print("\nThank you for using Brew Buddy Pro!")
print("\nDon't forget to clear the google sheet responses after the script is run.")
print("\nhttps://docs.google.com/spreadsheets/d/1PpeRo5NwWtCWgkyHn9dRoUrztqWxIX0mFlPERe4WtIU/edit?usp=sharing")
print("\n See you next time!")
