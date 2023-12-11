import json

with open("data.json", "r") as file:
    data = json.load(file)

# print(data)

for item in data:
    print("Object", item)
    for key, value in item.items():
        print("Key:", key, "Value:", value)
