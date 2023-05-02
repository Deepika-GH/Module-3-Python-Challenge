
import os
import csv

#read the file by providing the path of the file

election_csv = os.path.join("Resources","election_data.csv")

Analysis_file = os.path.join("analysis","Analysis.txt")

#initialize the variables

total = 0
candidateVotes = {}
candidates=[]

summary={"candidates" : "", "percentOfVotes" : 0,"totalVotes" : 0}

with open(election_csv) as csvfile,open(Analysis_file, "w") as outputfile:
     csvreader = csv.reader(csvfile,delimiter=",")
     print(csvreader)
#skip header    
     next(csvreader)
# loop though the data in file for analysis
     for row in csvreader:
          Ballot_ID = int(row[0])
          County = row[1]
          Candidate_Name = row[2]
# add the rows to get totol number of votes cast
          total += 1

# create empty list and add candidate names to the list of candidates
          if Candidate_Name not in candidates:
               candidates.append(Candidate_Name)
# if candidate name exists in the list add the votes of the candidates           
          if Candidate_Name in candidateVotes:
               candidateVotes[Candidate_Name] += 1
          else:
               candidateVotes[Candidate_Name] = 1
# print the output in text file
     outputfile.write("Election Results\n")
     outputfile.write("-----------------------------------------\n")
     outputfile.write(f"Total Votes: {total}\n")
     outputfile.write("-----------------------------------------\n")

#calculate vote % looping through the cadidates list crated in above step
     for candidate in candidates:
          vote_percentage = round((candidateVotes[candidate]/total)*100,3)

          outputfile.write(f"{candidate} : {vote_percentage}% ({candidateVotes[candidate]})\n")
     outputfile.write("-----------------------------------------\n")
     winner = max(candidateVotes, key=candidateVotes.get)
     outputfile.write(f"Winner: {winner}\n")
     outputfile.write("-----------------------------------------\n")

# print the results in the terminal
print(f"Election Results")
print(f"-------------------------------------------------------")
print(f"Total Votes: {total}")
print(f"-------------------------------------------------------")
for candidate in candidates:
     vote_percentage = round((candidateVotes[candidate]/total)*100,3)

     print(f"{candidate} : {vote_percentage}% ({candidateVotes[candidate]})")

print(f"-------------------------------------------------------")
winner=max(candidateVotes , key=candidateVotes.get)
print(f"Winner : {winner}")
print(f"-------------------------------------------------------")




      
     
          






