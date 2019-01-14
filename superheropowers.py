# load libraries
import json

# read superheroes.json
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

data = []

# print(superheroes)

# get the members
members = superheroes['members']

# print(members)

# loop through each member
for member in members:
	# for each member get a list of the powers
	powers = member['powers']
	# print(powers)

	# loop through the powers and print each one
	for power in powers:
		# print(power)
		data.append(power)

# print(data)

# Make the list unique
unique_powers = list(set(data))
print(unique_powers)