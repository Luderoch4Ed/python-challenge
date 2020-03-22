# Import required packages
import csv
import os

# Create dictionary
Election_Results = {} 
Percent = []

PyPoll_csv = "Resources/election_data.csv"

#Open Elecation data as csvfile:
with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader,None)

    # Lists to store data for financial Data
    Voter_Count=1
    startrow = next(csvreader)
            
    for row in csvreader:
        #calculate change in value
        politician = row[2]
        if politician in Election_Results.keys():
            Election_Results[politician] += 1
        else:
            Election_Results[politician] = 1
        
Voter_Count = sum(Election_Results.values()) 

#out put report header and total votes to text file
output = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {Voter_Count}\n"
    f"----------------------------\n"    
)
#output report header and Total votes to terminal
print(f"Election Results\n")
print("----------------------------")
print(f"Total Votes: {Voter_Count}")
print("----------------------------")            

#Loop through candidates for votes and percentage won
for i in Election_Results:
    Percent = round((float(Election_Results[i])/Voter_Count)*100,0)
    print(f" {i} : {Percent}% ({Election_Results[i]})")
    output += f" {i} : {Percent}% ({Election_Results[i]})\n"

#Loop through condidates results to determine winner
for w in Election_Results.keys():
    if Election_Results[w] == max(Election_Results.values()):
        winner = w

#Output of winner to file and terminal
print("----------------------------")        
print(f" The winner is : {winner}") 
print(f"----------------------------\n")            
output += (
    f"----------------------------\n"
    f"The winner is : {winner}\n"
    f"----------------------------\n"
)
        
# Set variable and filename for output file
output_file = os.path.join("Election_results.txt")

#  Open the output to text execution step
with open(output_file, "w") as textfile:
    textfile.write(output)
