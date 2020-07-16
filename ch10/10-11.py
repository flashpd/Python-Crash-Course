import json

filename = '10-11.json'
number = input("Please input you favorite number: ")
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

with open(filename) as f_obj:
    num = json.load(f_obj)
    print(num)
