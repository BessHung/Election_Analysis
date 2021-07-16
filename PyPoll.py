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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

#Read and print header row
    headers=next(file_reader)
    print(headers)

#initialize a total vote = 0  
    total_votes = 0

    for row in file_reader:
        total_votes += 1
print(total_votes)

# Using the with statement open the file as a text file.
# with open(file_to_save,'w') as txt_file:

#     txt_file.write('Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson')

