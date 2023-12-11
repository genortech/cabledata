import json

with open("data.json", "r") as file:
    data = json.load(file)

# Extract the first two key pairs from each object in the data set
extracted_key_pairs = []
for item in data:
    extracted_keys = list(item.keys())[:2]  # Get the first two keys
    extracted_values = [
        item[key] for key in extracted_keys
    ]  # Get the corresponding values
    extracted_key_pairs.append((extracted_keys, extracted_values))

# Split the values of the first two keys
for item, (keys, values) in zip(data, extracted_key_pairs):
    item[keys[0]] = values[
        0
    ].split()  # Update the conductor area key with a list of strings
    item[keys[1]] = values[
        1
    ].split()  # Update the insulation thickness key with a list of strings

# Remove the last key pair from each object in the data set
for item in data:
    del item[list(item.keys())[-1]]

# Split the data into a new list of objects, each containing a single set of values for the first two keys
updated_data = []
for item in data:
    for i in range(len(item[keys[0]])):
        new_item = {}
        for key in keys:
            new_item[key] = item[key][
                i
            ]  # Create a new object with a single set of values for the first two keys
        updated_data.append(new_item)

# Save the updated data set to a new JSON file
with open("updated_data.json", "w") as file:
    json.dump(updated_data, file, indent=2)
