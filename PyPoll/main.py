import os
import csv


election_csv = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join("..", "analysis", "analysis.txt")

total_votes = 0
candidates = []
candidate_votes = {}

# Read the election data
with open('election_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Calculate total number of votes
        total_votes += 1
        
        candidate_name = row['Candidate']
        if candidate_name not in candidate_votes:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1

# Calculate percentages and find the winner
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

winner = max(candidate_votes, key=candidate_votes.get)

for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += "-------------------------\n"

# Print the output 
print(output)

# Write the output to a text file
with open(output_path, "w") as txt_file:
    txt_file.write(output)