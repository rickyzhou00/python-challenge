#import modules

import csv
#set filepath
filepath = "python-challenge/PyBank/Resources/budget_data.csv"

#setting variables
datarows = 0
totalamount = 0
revenuechange = 0 
oldrevenue = 0 
changelist = [] 
datechange = []
averagechange = 0
greatestincrease = ["",0]
greatestdecrease = ["",9999999]

#opening csv file
with open(filepath) as csvfile:

    myData = csv.reader(csvfile)

    next(myData)

    for row in myData:
        #total number of months
        if any(row):
            datarows = datarows + 1
        #net total amount over the entire period
        totalamount = totalamount + float(row[1])

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        revenuechange = float(row[1]) - oldrevenue
        oldrevenue = float(row[1])
        changelist = changelist + [revenuechange]
        datechange = [datechange] + [row[0]]
        averagechange = sum(changelist)/len(changelist)
        roundedaveragechange = round(averagechange,2)
        #The greatest increase in profits (date and amount) over the entire period

        

        #The greatest decrease in profits (date and amount) over the entire period


    print("Total Months:",datarows)
    print("Total: $",totalamount)
    print("Average Change: $",roundedaveragechange)

#export analysis to text file with results
outputpath = "output.txt"
with open(outputpath,'w') as file:
    file.write("Financial Analysis")
    file.write("-------------------------")
    file.write(f"Total Months: {datarows}")
    file.write(f"Average Change:,{roundedaveragechange}")
