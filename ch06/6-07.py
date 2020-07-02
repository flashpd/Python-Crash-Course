person_1 = {
    'first_name': 'Panda',
    'last_name': 'Panda_2',
    'city': 'Sichuan'
}

person_2 = {
    'first_name': 'Tiger',
    'last_name': 'Tiger_2',
    'city': 'Dongbei'
}

person_3 = {
    'first_name': 'bird',
    'last_name': 'bird_2',
    'city': 'Beijing'
}

people = {
    'First_person': person_1,
    'Second_person': person_2,
    'Third_person': person_3
}

for person, person_info in people.items():
    print("\nUsername: " + person)

    fullname = person_info['first_name'] + person_info['last_name']
    print("\tFull name: " + fullname)
    print("\tCity: " + person_info['city'])