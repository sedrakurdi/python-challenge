#very similar to pybank exercise

# modules
import os
import csv

# variable / lists
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# path for original file
csvpath = os.path.join('C:\\Users\\sedra\\Desktop\\pythonHW\\pollinfo.csv')

# open & read file
with open(csvpath, newline='') as csvfile:

    # set variable, delimiter, initialize as reading the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # there is a header, read it first before the data
    csv_header = next(csvfile)

    # reading each row after the header
    for row in csvreader:
        
        # total # of votes
        total_votes += 1
        
        # specify & calculate total of votes per candidate
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # specify & calculate total of votes per candidate (percentage)
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # specify & calculate winner of the poll
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# print ...
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# output path
output_file = os.path.join('C:\\Users\\sedra\\Desktop\\pythonHW\\pypoll\\main.py')

# open output in write mode
with open(output_file, 'w',) as txtfile:

# write & print new data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
