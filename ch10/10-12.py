import json

def get_favorite_number():    
    filename = '10-11.json'
    with open(filename, 'r+') as f_obj:
        number = json.load(f_obj)

        if number:
            print(number)
        else:
            number = input("Please input you favorite number: ")
            json.dump(number, f_obj)

get_favorite_number()
