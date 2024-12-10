# PyBank

#imports
import csv
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

filepath = "Resources/budget_data.csv"

# Initialize variables
# These will be the outputs
total_months = 0 # How many months there are
net = 0 # What the total change is from beginning to end
average_prof = 0 # What the average profit/loss is each month
max_prof = 0 # The highest profit of a single month
prof_month = "" # The name of the month with the highest profit
max_loss = 0 # The greatest loss of a single Month
loss_month = "" # The name of the month with the greatest loss
# These are needed for the increasing and decreasing profit loops
last_prof = 0 # The profit or of the previous month
month_prof = 0 # This month's profit or loss
month_change = 0 # The difference between last month and this month's profit/loss



# Initialize reading CSV
# Drop the headers so that they are not calculated in.
# The next 6 lines are copied from Prof. Booth's 'starter' example.
with open(filepath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Now begin solving for each output
    for row in csvreader:
        # Total-months first
        total_months = total_months + 1

        # Net profit
        # The following line was copied from Professor Booth's example.
        net += int(row[1]) 

        # Average profit
        # Come back to this, it does not make sense to include it inside a loop. 

        # Greatest profit
        # This will require a loop, which will use it's own variables. 
        # The following 17 lines are copied from Prof.'s 'starter' example with variables changed.
        if total_months == 1:
            last_prof = int(row[1])
        else:
            # get change
            month_prof = int(row[1])
            change = month_prof - last_prof
            month_change += change
            # reset
            last_prof = month_prof
            # Check for new Min 
            if change < max_loss:
                max_loss = change
                loss_month = row[0]
            # Check for a new Max
            if change > max_prof:
                max_prof = change
                prof_month = row[0]

    #end loop by rows

    # Now back to the Average
average_prof = month_change / (total_months - 1)


# Create Output Summary and File
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net}
Average Change: ${round(average_prof, 2)}
Greatest Increase in Profits: {prof_month} (${max_prof})
Greatest Decrease in Profits: {loss_month} (${max_loss})
"""

# Print it
print(output) 

# File it
output_csv = "analysis/analyzed_budget_data.txt"

# The following 2 lines are copied from Prof's 'starter' example
with open(output_csv, "w") as txt_file:
    txt_file.write(output)


