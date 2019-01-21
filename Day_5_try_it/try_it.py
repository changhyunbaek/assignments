# import csv

# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     # Write header
#     writer.writerow(['col1', 'col2'])

#     # Write data
#     rows = [
#     ]
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])


# --------------------------------------------------------------------------------

# vegetables = [
#  {"name": "eggplant", "color": "purple"},
#  {"name": "tomato", "color": "red"},
#  {"name": "corn", "color": "yellow"},
#  {"name": "okra", "color": "green"},
#  {"name": "arugula", "color": "green"},
#  {"name": "broccoli", "color": "green"},
# ]

# # Write headers for CSV
# import csv

# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['name', 'color'])

#     # Loop through veggies
#     for vegetable in vegetables:
#     	# Write data
#     	name = vegetable['name']
#     	color = vegetable['color']
#     	row = [name, color]
#     	print(row)
#     	writer.writerow(row)				# cat testwrite.csv | csvlook


# --------------------------------------------------------------------------------


# import json

# rows = [
#     {"name": "Rachel", "age": 34},
#     {"name": "Monica", "age": 34},
#     {"name": "Phoebe", "age": 37}
# ]

# with open('testwrite.json', 'w') as f:
#     json.dump(rows, f, indent=2)


# --------------------------------------------------------------------------------


# import json

# # Open the file and put data in a variable
# with open('friends.json', 'r') as f:
#     friends = json.load(f)

# # Print
# # print(friends)



# # Write to a CSV file
# import csv

# with open('friends.csv', 'w') as f:
#     writer = csv.writer(f)

#     # Write header
#     writer.writerow(['name', 'age'])

#     for friend in friends:
#     	# {'name': 'Rachel', 'age': 34}
#     	name = friend['name']
#     	age = friend['age']
#     	writer.writerow([name, age])
#     	# print(friend)


# --------------------------------------------------------------------------------

# # Read veggies CSV file
# import csv
# import json

# with open('veggies.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)


# # Print rows
# # print(json.dumps(rows, indent=2))


# # Write json to a file
# with open('veggies.json', 'w') as f:
#     json.dump(rows, f, indent=2)

# --------------------------------------------------------------------------------


# # Read veggies CSV file
# import csv
# import json
# from pprint import pprint

# with open('veggies.csv', 'r') as f:
#     reader = csv.reader(f)
#     rows = list(reader)

# pprint(rows)


# --------------------------------------------------------------------------------

# import json


# # Reads superheroes.json
# import json

# with open('superheroes.json', 'r') as f:
#     superheroes = json.load(f)
    
# # print(superheroes)


# # Creates an empty array called powers
# all_powers = []

# # Loop through the members of the squad
# members = superheroes['members']
# for member in members:

# 	# and append the powers of each to the powers array.
# 	powers = member['powers']
# 	# print(powers)

# 	for power in powers:
# 		# print(power)
# 		all_powers.append(power)


# # Prints those powers to the terminal
# print(list(set(all_powers)))

# --------------------------------------------------------------------------------

# # Reads superheroes.json
# import json
# import csv


# # read superheroes.json
# with open('superheroes.json', 'r') as f:
#     superheroes = json.load(f)

# # print(superheroes)


# # save data for each member into a csv row
# with open('superheroes.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	headers = [
# 		'name',
# 		'age',
# 		'secretIdentity',
# 		'powers',
# 		'squadName',
# 		'homeTown',
# 		'formed',
# 		'secretBase',
# 		'active'
# 	]

# 	# Write header
# 	writer.writerow(headers)

# 	members = superheroes['members']

# 	# Loop over the members
# 	for member in members:

# 		# define variables
# 		name = member['name'],
# 		age = member['age'],
# 		secretIdentity = member['secretIdentity'],
# 		powers = member['powers'],

# 		squadName = superheroes['squadName'],
# 		homeTown = superheroes['homeTown'],
# 		formed = superheroes['formed'],
# 		secretBase = superheroes['secretBase'],
# 		active = superheroes['active']

# 		firstpower = member['powers'][0]

# 		# Write data to CSV file
# 		row = [
# 			name,
# 			age,
# 			secretIdentity,
# 			powers,
# 			squadName,
# 			homeTown,
# 			formed,
# 			secretBase,
# 			active
# 		]

# 		writer.writerow(row)


# --------------------------------------------------------------------------------


# friends = [
#     {"name": "Rachel", "age": 34},
#     {"name": "Monica", "age": 34},
#     {"name": "Phoebe", "age": 37}
# ]

# # filter to age < 37
# millenials = []

# for friend in friends:
# 	# friend = {"name": "Rachel", "age": 34}
#     if friend['age'] < 37:
#         millenials.append(friend)

# print(millenials)



# # filter whitelist names

# cool_people = []
# whitelist = ['Rachel', 'Phoebe']
# for friend in friends:
#     if friend['name'] in whitelist:
#         cool_people.append(friend)

# print(cool_people)



# filter blacklist names

# cool_people = []
# blacklist = ['Monica']
# for friend in friends:
#     if friend['name'] not in blacklist:
#         cool_people.append(friend)

# print(cool_people)


# --------------------------------------------------------------------------------

















