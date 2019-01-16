# Eric and Chang


#Read vegetables.csv
import csv
import json
from pprint import pprint

with open('vegetables.csv','r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

# Group by color
veggies_by_color = {}
for vegetable in vegetables:

    color = vegetable['color']

    if color in veggies_by_color:
        veggies_by_color[color].append(vegetable)

    else:
        veggies_by_color[color] = [vegetable]



# Print to terminal
pprint(veggies_by_color)

# Output to JSON file
with open('veggies_by_color.json','w') as f:
    json.dump(veggies_by_color, f, indent=2)





