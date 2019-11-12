import csv

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open("Resources/election_data.csv") as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        # If candidates not in option, append name to option
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Initialize vote count in the dictionary
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Export to text
with open("analysis/election_analysis.txt", "a") as txt:
    election_results = (f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results)

    txt.write(election_results)

    # Loop and reassign winner for greater votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})"
        print(voter_output)

        txt.write(voter_output)

    winner_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winner_summary)

    # Save the winning candidate's name to the text file
    txt.write(winner_summary)
