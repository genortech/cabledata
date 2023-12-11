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

# print(extracted_key_pairs)

# Remove the first two key pairs from each object in the data set
for item, (keys, _) in zip(data, extracted_key_pairs):
    for key in keys:
        del item[key]

# Also remove the last key pair from each object in the data set
for item in data:
    del item[list(item.keys())[-1]]

# print(data)
new_data = []
for item in data:
    # print(item)
    for key in item:
        # print(key)
        # print(item[key])
        split_data = item[key].split()
        # print(split_data)
        temp_data = [item for item in split_data]
        print(temp_data)
        new_data = [{str(key): item} for item in temp_data]
        print(json.dumps(new_data))

# Save the updated data set to a new JSON file
with open("updated_data.json", "w") as file:
    json.dump(data, file, indent=2)
