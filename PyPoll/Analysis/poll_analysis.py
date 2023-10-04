import csv

my_report = open('Analysis/poll_report.txt','w')
poll_data = ("/Users/brandonrogers/Desktop/Data Analyst/Projects/Python Challenge/PyPoll/Resources/election_data.csv")
with open (poll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    total_votes = 0
    candidates = {}
  
    for row in csv_reader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate]= candidates.get(candidate, 0) + 1


results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

winner = max(results, key=lambda x: x[2])

output = f'''
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
'''
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# ''' 

for candidate, percentage, votes in results:
    output+= f"{candidate}: {percentage:.3f}% ({votes})\n"
    
output+=f"-------------------------\nWinner: {winner[0]}\n-------------------------"


print(output)
my_report.write(output)