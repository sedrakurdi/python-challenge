#modules
import os
import csv

# setting variables
months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# original file path
csvpath = os.path.join('C:\\Users\\sedra\\Desktop\\pythonHW\\bankinfo.csv')

# open & read csv file
with open(csvpath, newline='') as csvfile:
    
    # delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # there is a header row, skip it
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # get total # of months
    # net amount of profit and losses
    # set variables for rows
    previous_row = int(row[1])
    months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # read each row not including the header
    for row in csvreader:
        
        # get total number of months
        months += 1
        # get net amount
        net_amount += int(row[1])

        # get change from month to month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # average
    # date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# print
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Months: {months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# output path
output_file = os.path.join('C:\\Users\\sedra\\Desktop\\pythonHW\\pybank\\main.py')

# open file with write mode
with open(output_file, 'w',) as txtfile:

# writing the new data with calculations
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")