import csv


# # Write a CSV file
# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])


# # Read from a CSV file
# with open('testwrite.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# for row in rows:
#     print(row)


vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]



# Open a CSV file
with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])

	# Loops through vegetables and prints out all the vegitables
	for vegetables in vegetables:

		#Write each veggie to a CSV
		name = vegetables['name']
		color = vegetables['color']

		row = [name, color]

		writer.writerow(row)