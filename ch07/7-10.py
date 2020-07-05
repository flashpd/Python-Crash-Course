positions = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    position = input("If you could visit one place in the world, where would you go? ")

    positions[name] = position

    repeat = input("Would you like to visit another place!(yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Result ---")
for name, position in positions.items():
    print(name + " would like to visit " + position + ".") 