# PyPoll.py

#imports
import csv
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

filepath = "Resources/election_data.csv"

# Initialize variables
# These will be the outputs
vote_total = 0
candidates = {}
most_votes = 0
# We need a variable for the percentage each candidate received, but we need to determine who the candidates were first. 
# We need a variable for the number of votes each candidate received, but we need to determine who the candidates were first. 
winner = ""

# Initialize reading CSV
# Drop the headers so that they are not calculated in.
# The next 6 lines are copied from the PyBank.py activity.
with open(filepath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # First determine how many votes were cast.
    for row in csvreader:
        vote_total = vote_total + 1

        #The following 6 lines were copied from Professor Booth's example with variables changed.
        # Track votes
        vote_for = row[2]
        if vote_for in candidates.keys():
            candidates[vote_for] += 1 # add one to the value
        else:
            candidates[vote_for] = 1 # initialize with one vote

# "candidates" now shows vote counts per candidate
# Now must determine percentage of votes
# The following block of code was taken from an instructor example. In order to use it, two new variables must be initialized.
win_vote_count = 0
results = ""
# The following 10 lines were taken from Prof.'s example with variables changed
for vote_for in candidates.keys():
    votes = candidates[vote_for] # get votes (value) for that key
    vote_percent = round(100 * votes / vote_total, 3)

    if votes > win_vote_count:
        # we have a new winner
        win_vote_count = votes
        winner = vote_for

    # create output
    text = f"{vote_for}: {vote_percent}% ({votes})\n"
    results += text

    # Determine what the greatest number of votes was
    if votes > most_votes:
        most_votes = votes
        # Name the winner
        winner = vote_for

# Create Output Summary and File
output = f"""
Election Results
-------------------------
Total Votes: {vote_total}
-------------------------
{results}
-------------------------
Winner: {winner}
-------------------------
"""

# Print it
print(output) 

# File it
output_csv = "analysis/analyzed_election_data.txt"

# The following 2 lines are copied from Prof's 'starter' example
with open(output_csv, "w") as txt_file:
    txt_file.write(output)
 