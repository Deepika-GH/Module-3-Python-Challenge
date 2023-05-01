

import os
import csv
#Read the file from resources folder And define where output file should be stored

budget_csv=os.path.join("Resources","budget_data.csv")

Analysis_file = os.path.join("analysis", "Analysis.txt")

# set initial values to the variables needed in output
Total_Months = 0
Total = 0
previous_profit_loss = 0
ChangeTotal = 0
Greatest_Increase = {"date": "", "amount": 0}
Greatest_Decrease = {"date": "", "amount": 0}

with open(budget_csv) as csvfile,open(Analysis_file, "w") as outputfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #print(csvreader)
#skip header    
    next(csvreader)    

# loop through data in csv file for each row
    for row in csvreader:
        Date=row[0]
        Profit_Losses=int(row[1])
        
        Total_Months += 1

        Total += Profit_Losses
# to calculate profit/loss changes throughout the file
   # set the changes to start from month 2 skipping month1
        if Total_Months > 1:
    # calculate change for each month
            change = Profit_Losses - previous_profit_loss
            ChangeTotal += change

    # Determine the greatest increase in profits
            if change > Greatest_Increase["amount"]:
                Greatest_Increase["date"] = row[0]
                Greatest_Increase["amount"] = change
            elif change < Greatest_Decrease["amount"]:
                Greatest_Decrease["date"] = row[0]
                Greatest_Decrease["amount"] = change

        previous_profit_loss = Profit_Losses

      #calulate average change

    avg_change = round(ChangeTotal / (Total_Months - 1), 2)
    
    outputfile.write("Financial Analysis\n")
    outputfile.write("-------------------------------------------------------\n")
    outputfile.write(f"Total Months: {Total_Months}\n")
    outputfile.write(f"Total: ${Total}\n")
    outputfile.write(f"Average Change:{avg_change}\n")
    outputfile.write(f"Greatest Increase in Profits: {Greatest_Increase['date']} (${Greatest_Increase['amount']})\n")
    outputfile.write(f"Greatest Decrease in Profits: {Greatest_Decrease['date']} (${Greatest_Decrease['amount']})\n")

    