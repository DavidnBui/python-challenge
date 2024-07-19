import csv
import os

file_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')
output_file = os.path.join('PyPoll', 'Analysis', 'election_results.txt')

total_votes = 0
candidate_votes = {}

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    print(f"Header: {header}")

    try:
        candidate_index = header.index("Candidate")
    except ValueError:
        print("Candidate column not in header")
        exit()

    for row in csv_reader:
        if len(row) < len(header):
            print(f"Skip Incomplete Row: {row}")
            continue

        total_votes += 1
        candidate = row[candidate_index]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_file = 'PyPoll\Analysis\election_results.txt'
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")