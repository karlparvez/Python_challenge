
import os
import csv


csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")


total_votes = 0
candidate = ""
candidate_list = []
vote_list = []
percent_list = []
winner = ""


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
    csv_header = next(csvreader)
    
    
    for row in csvreader:
        
        total_votes += 1
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1
        
percent_list = [(100/total_votes) * x for x in vote_list]


winner = candidate_list[vote_list.index(max(vote_list))]

       
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for x in candidate_list:
    print(x + ": " + str(format(percent_list[candidate_list.index(x)], '.3f')) 
        + "% (" + str(vote_list[candidate_list.index(x)]) + ")")
    
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")


f = open("analysis.txt", "w")

print("Election Results\n")
print("-------------------------\n")
print("Total Votes: " + str(total_votes) + "\n")
print("-------------------------\n")

for x in candidate_list:
    print(x + ": " + str(format(percent_list[candidate_list.index(x)], '.3f')) 
        + "% (" + str(vote_list[candidate_list.index(x)]) + ")\n")
    
print("-------------------------\n")
print("Winner: " + winner + "\n")
print("-------------------------\n")
