pizzas = ['one', 'two', 'three']
for pizza in pizzas:
    print("I like " + pizza + " pizza")

print("I really love pizza!")

friend_pizzas = pizzas[:]
friend_pizzas.append("four")
for pizza in pizzas:
    print("My favorite " + pizza + " pizza")

for friend_pizza in friend_pizzas:
    print("My friend favorite " + friend_pizza + " pizza")