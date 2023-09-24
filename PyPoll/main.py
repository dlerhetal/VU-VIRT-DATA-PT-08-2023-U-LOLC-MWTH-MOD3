import os
import csv
from collections import defaultdict

# Create a dictionary to store counts of unique values in column B (index 1)
CountCandidates = defaultdict(int)

# Open the data file in read mode ('r')
election_data = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Ignore the header row
    header = next(csvreader)
    
    #Count rows for Total Votes and the final column for individual results
    CountRows = 0
    for row in csvreader:
            CountRows += 1
            Candidate = row[2]
            CountCandidates[Candidate] += 1
          
#Which of the values in the final column is counted most often
MaxCount = max(CountCandidates, key=CountCandidates.get)

#Print report header and number of Total Votes
print(f"Election Results:\n")
print(f"-------------------------\n")
print(f"Total Votes: {CountRows}\n")
print(f"-------------------------\n")            

#Print each candidate name as well as their corresponding percent and total.
for value, count in CountCandidates.items():
    PercentVote = round(((count/CountRows)*100),2)  
    print(f"{value}: {PercentVote}% ({count})\n")

#Prting the name of the winner
print(f"-------------------------\n \n Winner: {MaxCount}\n")
print(f"-------------------------\n")

# Define the file path for the report
report_file = os.path.join('..', 'PyPoll', 'Analysis', 'Results.txt')

# Open the report file in write mode ('w')
with open(report_file, 'w') as report:
    report.write("Election Results\n")
    report.write("\n")
    report.write("-------------------------\n")
    report.write("\n")
    report.write(f"Total Votes: {CountRows}\n")
    report.write("\n")
    report.write("-------------------------\n")
    report.write("\n")
    for value, count in CountCandidates.items():
        PercentVote = round(((count/CountRows)*100),2)
        report.write(f"{value}: {PercentVote}% ({count})\n  \n")
    report.write("-------------------------\n")
    report.write("\n")
    report.write(f"Winner: {MaxCount}")
    report.write("\n")
    report.write("\n")
    report.write("-------------------------\n")
print(f"Report has been written to {report_file}")
