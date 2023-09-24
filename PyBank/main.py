import os
import csv

CountRows = 0
PLTotal = 0
PLValues = []
MaxIncrease = 0
MaxDecrease = 0
DataValues = []

# Open the data file in read mode ('r')
with open(os.path.join('..', 'PyBank','Resources', 'budget_data.csv'), 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    PL = None
    DailyRow = None

# Subtract the current row from the next row to determine Max Increase/Decrease
    for row in csvreader:
        if DailyRow is not None:
            CurrentData = int(DailyRow[1])
            NextData = int(row[1])            
            DataDifference = NextData - CurrentData
            DataValues.append(DataDifference)            
            if DataDifference > MaxIncrease:
                MaxIncrease = DataDifference
                IncreaseDate = row[0]
            elif DataDifference < MaxDecrease:
                MaxDecrease = DataDifference
                DecreaseDate = row[0]
                
        DailyRow = row

# Count the Total Months and sum the total P/L      
        if len(row) == 2:
            CountRows += 1
            PL = float(row[1])
            PLTotal += PL
            PLValues.append(row[1])
            PLPrint = round(PLTotal)

# Determine the Average Change            
if PLValues:
    FirstRow = int(PLValues[0])
    FinalRow = int(PLValues[-1])
    AverageChange = round((FinalRow - (FirstRow)) / (CountRows - 1), 2)    

# Define the file path for the report
report_file = os.path.join('..', 'PyBank','Analysis', 'results.txt')

# Open the report file in write mode ('w')
with open(report_file, 'w') as report:
    report.write("Financial Analysis\n")
    report.write("\n")
    report.write("------------------\n")
    report.write("\n")
    report.write(f"Total Months: {CountRows}\n")
    report.write("\n")
    report.write(f"Total: ${PLPrint}\n")
    report.write("\n")
    report.write(f"Average Change: ${AverageChange}\n")
    report.write("\n")
    report.write(f"Greatest Increase in Profits: {IncreaseDate} (${MaxIncrease})\n")
    report.write("\n")
    report.write(f"Greatest Decrease in Profits: {DecreaseDate} (${MaxDecrease})\n")

# Print the results here
print("Financial Analysis\n")
print("------------------\n")
print(f"Total Months: {CountRows}\n")
print(f"Total: ${PLPrint}\n")
print(f"Average Change: ${AverageChange}\n")
print(f"Greatest Increase in Profits: {IncreaseDate} (${MaxIncrease})\n")
print(f"Greatest Decrease in Profits: {DecreaseDate} (${MaxDecrease})\n")
print(f"Report has been written to {report_file}")