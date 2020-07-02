nation_river = {
    'Nile': 'egypt',
    'Yangtze': 'China',
    'Mississippi': 'America'
}

for nation, river in nation_river.items():
    print("The " + nation + " runs throught " + river + ".")

print("\n")

for nation in nation_river.keys():
    print(nation)

print("\n")

for river in nation_river.values():
    print(river)