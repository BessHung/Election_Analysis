
'''
counties1 = ["Arapahoe","Denver","Jefferson"]
if counties1[1]=="Denver":
    print (counties1[1])

temperature=int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#What is the score?
score = int(input("What is your test score? "))

#Determin the grade
if score >= 90:
    print('Your grade is an A.')
else:
    if score>= 80:
        print('Your grade is a B.')
    else:
        if score >=70:
            print('Your grade is a C.')
        else:
            if score>= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is a F.')

#rewrite
score2 = int(input("What is your test score? "))

#Determin the grade
if score2 >= 90:
    print('Your grade is an A.')
elif score2>= 80:
    print('Your grade is a B.')
elif score2 >=70:
    print('Your grade is a C.')
elif score2>= 60:
    print('Your grade is a D.')
else:
    print('Your grade is a F.')


counties2 = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties2:
    print('El Paso is in the list of counties.')
else:
    print('El Paso is not in the list of counties.')

if "Arapahoe" and "El Paso" in counties2:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print('Arapahoe or El Paso are not in the list of counties.')

if "Arapahoe" or "El Paso" in counties2:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print('Arapahoe and El Paso are not in the list of counties.')

#List
counties = ["Arapahoe","Denver","Jefferson"]

or county in counties:
    print(county)
for num in range(5):
    print(num)
for i in range(len(counties)):
        print(counties[i])

#dictionary
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.")

#List of dictionary
voting_data=[{'county':'Arapahoe','registered_voters':422829},{'county':'Denver', 'registered_voters': 463353},{'county':'Jefferson', 'registered_voters': 432438}]

for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):
    print(voting_data[county]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])
    print(county_dict['county'])


#print1
candidate_votes=int(input("How mant votes did the candidate get in the election? "))
total_votes=int(input("What is the total number of votes in the election? "))
message_to_candidate=(
    f"You received {candidate_votes:,} number of votes.\n" 
    f"The total number of votes in the election was {total_votes:,}. \n"
    f"You received {candidate_votes / total_votes *100:.2f}% of the total votes."
)

print(message_to_candidate)


#print2
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    message = (
        f"{county} has {voters:,} registered voters."
    )
    print(message)
'''

#print3
voting_data=[{'county':'Arapahoe','registered_voters':422829},{'county':'Denver', 'registered_voters': 463353},{'county':'Jefferson', 'registered_voters': 432438}]

for county_dict in voting_data:
    message=(
        f"{county_dict['county']} has {county_dict['registered_voters']:,} registered voters."
)
    print(message)

