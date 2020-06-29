# places = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou']
places = ['h', 'e', 'l', 'l', 'o']

print('0---', end='')
print(places)

print('1---', end='')
print(sorted(places))

print('2---', end='')
print(places)

print('3---', end='')
print(sorted(places, reverse=True))

print('4---', end='')
print(places)

places.reverse()
print('5---', end='')
print(places)

places.reverse()
print('6---', end='')
print(places)

places.sort()
print('7---', end='')
print(places)

places.sort(reverse=True)
print('8---', end='')
print(places)
