# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

#Direct Path to the File
# import csv

# file_to_load = 'Resources\election_results.csv'

# with open(file_to_load,encoding='utf-8') as election_data:
#     print(election_data)


#Indirect Path to the File

import csv
import os
# Assign a variable for the file to load and save the file.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join('analysis','election_analysis.txt')

#Declare a list for candidate
candidate_options = []

#Declare a dictionary for candidate votes
candidate_votes={}

#Declare winning variable
winning_candidate=''
winning_count= 0
winning_percentage= 0

#initialize a total vote = 0  
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

#Read and print header row
    headers=next(file_reader)
    #print(headers)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #append candidate name in candidate_option list
            candidate_options.append(candidate_name)
            # start counting candidate's votes
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

    #The percentage of candidate's votes
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine the winning vote count and candidate
        if votes > winning_count and vote_percentage>winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------"
    )
    print(winning_candidate_summary)


#print(candidate_votes)
#print(candidate_options)
#print(total_votes)

# Using the with statement open the file as a text file.
# with open(file_to_save,'w') as txt_file:

#     txt_file.write('Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson')

