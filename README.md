# Election_Analysis

## Project Overview
Complete the election audit and provide the election results needed by the Colorado Board of Elections.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.58.2

## Election-Audit Results

[Election analysis](https://github.com/BessHung/Election_Analysis/blob/ba7452990fc684e449b0caa811ee421b9a962b0b/analysis/election_analysis.txt)

The analysis of the election show that:
- Total number of votes cast: 369,711 votes cast
- Election results in each county:
1.	Jefferson: 10.5% (38,855)
2.	Denver: 82.8% (306,055)
3.	Arapahoe: 6.7% (24,801)
- The largest number of the county: Denver
- Election results of each candidate:
1.	Charles Casper Stockham: 23.0% (85,213)
2.	Diana DeGette: 73.8% (272,892)
3.	Raymon Anthony Doane: 3.1% (11,606) 
- The winner of the election: Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.



## Election-Audit Summary
Using the script below to read each row of the csv file and get the list of the candidate’s name and county’s name. In the first part of repetition statement, `For` loop, it is reading each row of the csv file, and using row[index] to get the value. Next, inside the for loop, using conditional statements, `If`, to extract the unique value and append the data in the list and dictionary. In conclusion, with some modifications such as the index number, header name or the conditional statements, the script can be used in reading any csv files. 
```Python
# For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
Using the script below to read and calculate the data from the list and dictionary. In the first part of repetition statement, `For` loop, it retrieves the votes count and calculates the percentage for each county from the dictionary, then print out the result of each item. Next, inside the for loop, using conditional statements, `If`, to get the largest number of the county. To sum up, the script can be used in grabbing the data, doing some math for each item from the dictionary. Further, return the expectation data by using if-statements.
```Python
    # 6a: Write a for loop to get the county from the county dictionary
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes_count = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        votes_percentage = float(votes_count) / float(total_votes) *100
        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {votes_percentage:.1f}% ({votes_count:,})\n")
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if votes_count > winning_county_count:
            winning_county_count = votes_count
            winning_county = county_name
    # 7: Print the county with the largest turnout to the terminal.
    winning_county_results = (
        f"-------------------------\n"
        f"The largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_results)
```
