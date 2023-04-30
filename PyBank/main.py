
#Read the file from resources folder

import os

import csv

budget_csv=os.path.join("Resources","budget_data.csv")


with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    print(csvreader)
#skip header    
    next(csvreader)
    
# initialize variables needed to be calculated in the output
    Total_Months=0
    Total=0
    Changes=[]
    Greatest_Increase=0
    Greatest_Inc_Mon=""
    Greatest_Decrease=0
    Greatest_Dec_Mon=""

#loop through csv file for each row

    for row in csvreader:
        Date=row[0]
        Profit_losses=int(row[1])
# add the rows to get totol number of months
        Total_Months += 1
# add the rows of second index in row to get net total amount
        Total += Profit_losses
#print(f"Total: ${Total}")

# Calculate the change in profit/loss since the previous row
       
        if len(Changes) == 0:
            change = 0
        else:
            change = Profit_losses - Changes[-1]
        Changes.append(change)

# Calculate the average change
        avg_change = sum(Changes) / len(Changes)
print(f"Average Change: ${avg_change}")

"""# Check if this is the greatest increase or decrease in profit/loss so far
        Greatest_Increase =max(Changes)
        Greatest_Decrease =min(Changes)
        Greatest_Inc_Mon=Date(Changes.index(Greatest_Increase+1))
        Greatest_Dec_Mon=Date(Changes.index(Greatest_Decrease+1))




# Print the analysis results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {Greatest_Inc_Mon} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Dec_Mon} (${Greatest_Decrease})")
"""

       

    




