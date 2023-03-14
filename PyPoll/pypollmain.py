#import modules
import os
import csv

#set filepath
filepath = os.path.join("python-challenge/PyPoll/Resources/election_data.csv")

#setting variables
totalvotes = 0
candidatevotes = {}
candidatelist = []
winnervote = 0
winner = ""
#opening csv file
with open(filepath) as csvfile:
    csvreader = csv.DictReader(csvfile,delimiter=",")

    for row in csvreader:
        totalvotes = totalvotes + 1

        candidates = row["Candidate"]
        if candidates in candidatelist:
            candidatevotes[candidates] = candidatevotes[candidates] + 1
        else:
            candidatelist.append(candidates)
            candidatevotes[candidates] = 1
    

#output
print("Election Results")
print("------------------------")
print(f"Total Votes: {totalvotes}")



#output to text
outputpath = "pypolloutput.txt"
with open(outputpath,'w') as file:
    file.write("Election Results")
    file.write("-------------------------")
    file.write(f"Total Votes: {totalvotes}")
    file.write("--------------------------")
    

    for candidates in candidatevotes:
        voters = candidatevotes[candidates]
        percentage = voters/totalvotes * 100
        
        if voters>winnervote:
            winnervotes = voters
            winner = candidates
        output = (f"{candidates}:{percentage:3f}%({voters})")
        print(output)
        file.write(output)