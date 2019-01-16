# Reads superheroes.json
import json
import csv


# read superheroes.json
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

# print(superheroes)


# save data for each member into a csv row
with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	headers = [
		'name',
		'age',
		'secretIdentity',
		'powers',
		'squadName',
		'homeTown',
		'formed',
		'secretBase',
		'active'
	]

	# Write header
	writer.writerow(headers)

	members = superheroes['members']

	# Loop over the members
	for member in members:

		# define variables
		name = member['name'],
		age = member['age'],
		secretIdentity = member['secretIdentity'],
		powers = member['powers'],

		squadName = superheroes['squadName'],
		homeTown = superheroes['homeTown'],
		formed = superheroes['formed'],
		secretBase = superheroes['secretBase'],
		active = superheroes['active']

		firstpower = member['powers'][0]

		# Write data to CSV file
		row = [
			name,
			age,
			secretIdentity,
			powers,
			squadName,
			homeTown,
			formed,
			secretBase,
			active
		]

		writer.writerow(row)