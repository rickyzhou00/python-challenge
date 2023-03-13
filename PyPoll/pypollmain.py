#import modules
import os
import csv

#set filepath
filepath = os.path.join("python-challenge/PyPoll/Resources/election_data.csv")

#setting variables
totalvotes = 0
candidatevotes = {}


#opening csv file
with open(filepath) as csvfile:
    csvreader = csv.DictReader(csvfile)

    next(csvreader)

    for row in csvreader:
        totalvotes = totalvotes + 1
        candidate = row[2]

        if candidate in candidatevotes:
            candidatevotes = candidatevotes[candidate] + 1
        
        else candidatevotes[candidate] = 1


#output
print(totalvotes)
print(candidatevotes)
