
import os
import csv

#read the file by providing the path of the file

election_csv = os.path.join("Resourses","election_data.csv")

Analysis_file = os.path.join("analysis","Analysis.txt")

#initialize the variables

total = 0
percentOfVotes = 0
totalVotes = 0

with open(election_csv) as csvfile,open(Analysis_file, "w") as outputfile:
     csvreader=csv.reader(csvfile,delimiter=",")
     print(csvreader)
#skip header    
     next(csvreader)    






