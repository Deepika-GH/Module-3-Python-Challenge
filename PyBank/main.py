
#Read the file from resources folder

import os

import csv

budget_csv=os.path.join("Resources","budget_data.csv")

#list to store file data

date_Month=[]
profit_losses=[]

with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    print(csvreader)
    next

    Total_Months=