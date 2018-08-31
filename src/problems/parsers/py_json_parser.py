import json

with open('json_data.json', 'r') as f:
    data_dict = json.load(f)

for car in data_dict['vehicles']:
    car = car['car']
    print("-----CAR-----")
    print("Name:", car['name'])
    print("Model:", car['model'])
    print("Speed:", car['speed'])
