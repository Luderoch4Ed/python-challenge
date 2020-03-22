# Import required packages
import csv
import sys
import os

PyBank_csv = "Resources/budget_data.csv"

# with open(udemy_csv) as csvfile:
with open(PyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader,None)

    # Lists to store data for financial Data
    Period_count=1
    startrow=next(csvreader)
    Net_Revenue =0
    Net_Revenue = Net_Revenue+int(startrow[1])
    MonthlyChange = []
    length = []
    previous=int(startrow[1])
    changein_profit=0
    MonthlyChange = [] 
    MaxChange={"date":startrow[0],"value":0}
    MinChange={"date":startrow[0],"value":0} 

    for row in csvreader:
        #calculate change in value
        Period_count = Period_count+1 
        Net_Revenue = Net_Revenue+int(row[1])
        changein_profit = int(row[1])-previous 
        previous = int(row[1])    

        
        #Determine minimum and maximum change  in profit/loss and corresponding month
        if len(MonthlyChange) > 0 and changein_profit > max(MonthlyChange):
            MaxChange["date"] = row[0]
            MaxChange["value"] = changein_profit

        elif len(MonthlyChange) > 0 and changein_profit < min(MonthlyChange):
            MinChange["date"] = row[0]
            MinChange["value"] = changein_profit
 
        MonthlyChange.append(changein_profit)

    #Average of net change calculation
    NetChangeAvg = sum(MonthlyChange)/len(MonthlyChange)
          
#print out Financial summery of profit & loss for period provided

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Period_count}")   
print(f"Total: ${Net_Revenue}")
print(f"Average Change: $ {NetChangeAvg:.2f}")
print("Greatest Increase in Profits:",MaxChange["date"] , "($", MaxChange["value"],")")
print("Greatest Decrease in Profits:",MinChange["date"], "($", MinChange["value"],")")

# Zip lists together
#cleaned_csv = zip(DateVal, Net_Revenue)

# Set variable for output file
output_file = os.path.join("budget_final.txt")

#  Open the output file
sys.stdout = open(output_file, "w")
#Output Financial summery of profit & loss   
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Period_count}")
print(f"Total: ${Net_Revenue}")
print(f"Average Change: $ {NetChangeAvg:.2f}")
print("Greatest Increase in Profits:",MaxChange["date"] , "($", MaxChange["value"],")")
print("Greatest Decrease in Profits:",MinChange["date"], "($", MaxChange["value"],")")

sys.stdout.close()
    
